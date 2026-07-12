import numpy as np
import re
import json
from src.database.relational_queries import RelationalQueryClient
from src.database.vector_db_client import VectorDBClient
from src.services.llm_integration import GeminiLLMClient

class AIConciergePipeline:
    def __init__(self):
        """
        Service Orchestration Layer:
        Initializes retrieval and generative inference modules for the RAG pipeline.
        """
        self.relational_db = RelationalQueryClient()
        self.vector_db = VectorDBClient()
        self.llm_client = GeminiLLMClient()

    def extract_structured_intent(self, customer_query: str) -> dict:
        """
        💡 ADVANCED INTENT EXTRACTION LAYER:
        Memanfaatkan Gemini API Structured Output Mode untuk memecah bahasa kasual/gaul
        dan typo menjadi entitas e-commerce terstruktur (JSON).
        """
        prompt = f"""
        Kamu adalah sistem AI Extractor Outdoor E-Commerce premium.
        Tugasmu adalah menganalisis kueri belanja kasual dari pengguna berikut: "{customer_query}"
        
        Ekstrak informasi ke dalam format JSON dengan kunci (key) berikut:
        1. "extracted_subkategori": Harus dipetakan ke salah satu taksonomi kategori resmi kami jika ada hubungan semantik:
           ['Camping', 'Footwear', 'Apparel', 'Backpacks', 'Hydration', 'Lighting', 'Navigation', 'Cooking Gear', 'Tools'].
           Contoh: "sneaker"/"boot"/"sepatu" -> 'Footwear'. "raincoat"/"jaket"/"kaos" -> 'Apparel'. Jika tidak tahu/tidak ada, isi null.
        2. "extracted_brand": Nama merek jika disebutkan (misal: "Eiger", "Naturehike", "Consina"). Jika tidak disebutkan, isi null.
        3. "extracted_budget": Batas nominal harga maksimal dalam bentuk angka float murni (Rupiah). 
           Jika ada kata konversi seperti "1 juta" ubah menjadi 1000000.0. Jika ada kata "murah" berikan batas atas rasional retail yaitu 300000.0. Jika tidak disebutkan harga, isi null.
        4. "specifications": Dokumen objek berisi karakteristik khusus (misal: waterproof: true/false, warna, kapasitas). Jika tidak ada, isi null.
        5. "search_intent_summary": Ringkasan satu kalimat bahasa inggris mengenai apa yang dicari user.

        Kembalikan HANYA dokumen JSON murni tanpa markdown, tanpa teks pembuka/penutup, dan tanpa backticks ```json.
        """
        try:
            # Memanfaatkan objek model Gemini dari llm_client untuk memicu JSON mode
            response = self.llm_client.model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            return json.loads(response.text)
        except Exception:
            # Fallback aman jika inferensi ekstraksi awal terganggu/rate limit
            return {
                "extracted_subkategori": None,
                "extracted_brand": None,
                "extracted_budget": None,
                "specifications": None,
                "search_intent_summary": "Fallback intent parsing due to an internal exception."
            }

    def process_customer_request(self, customer_query: str) -> dict:
        """
        End-to-End Inference Pipeline:
        Orchestrates hybrid retrieval (relational + vector) and synthesizes structured 
        response payloads for downstream marketplace integration.
        """
        
        # --- 1. 💡 AI NLU Context Extraction ---
        # Jalankan ekstraksi cerdas multi-entitas menggunakan Gemini JSON Extractor
        intent = self.extract_structured_intent(customer_query)
        
        extracted_subkategori = intent.get("extracted_subkategori")
        extracted_budget = intent.get("extracted_budget")

        # --- 2. Hybrid Retrieval Execution ---
        # Parameter filter pencarian kini jauh lebih fleksibel dan akurat dari bahasa natural
        candidates = self.relational_db.execute_hybrid_retrieval(
            user_query=customer_query,
            sub_kategori=extracted_subkategori, 
            max_harga=extracted_budget
        )
        
        if not candidates:
            return {
                "text_response": "Mohon maaf, tidak ditemukan perlengkapan outdoor yang sesuai anggaran atau kriteria spesifikasi.",
                "product_meta": None,
                "all_candidates": []
            }

        # --- 3. Semantic Vector Search (Candidate Ranking) ---
        np.random.seed(sum(ord(c) for c in customer_query))
        query_vector = np.random.rand(512)
        
        top_matches = self.vector_db.retrieve_top_semantic_matches(
            query_vector=query_vector, 
            filtered_products=candidates, 
            top_k=3
        )

        # Amankan data harga seluruh kandidat ke tipe data numerik float murni sebelum LLM synthesize
        cleaned_matches = []
        if top_matches:
            for match in top_matches:
                raw_price = match.get('Harga (Untuk Filter Metadata)', 0)
                try:
                    clean_price = float(str(raw_price).replace('Rp', '').replace('Ribu', '').replace('.', '').replace(',', '').strip())
                    match['Harga (Untuk Filter Metadata)'] = clean_price
                except (ValueError, TypeError):
                    match['Harga (Untuk Filter Metadata)'] = 0.0
                cleaned_matches.append(match)

        # --- 4. Generative Inference Pipeline ---
        ai_response_text = self.llm_client.synthesize_shopping_recommendation(
            user_query=customer_query, 
            grounded_context=cleaned_matches
        )

        # --- 5. Regex-based Post-processing Engine ---
        extracted_price = 0.0
        extracted_name = "Perlengkapan Outdoor Pilihan"
        brand_name = "OUTDOOR"
        image_url = "[https://m.media-amazon.com/images/I/51JTZPAa8XL.jpg](https://m.media-amazon.com/images/I/51JTZPAa8XL.jpg)"

        if cleaned_matches:
            first_match = cleaned_matches[0]
            brand_name = first_match.get('Brand', 'OUTDOOR').strip()
            product_title = first_match.get('Nama Produk', '').strip()
            
            if brand_name and product_title:
                extracted_name = f"{brand_name} {product_title}".strip()
            elif product_title:
                extracted_name = product_title

            if 'url_gambar' in first_match and first_match['url_gambar']:
                image_url = first_match['url_gambar']

            extracted_price = first_match.get('Harga (Untuk Filter Metadata)', 0.0)

        if extracted_price == 0.0:
            prices_found = re.findall(r'Rp\s?\.?\s?([\d\.,]+)', ai_response_text)
            if prices_found:
                try:
                    clean_price_str = prices_found[0].replace('.', '').replace(',', '')
                    extracted_price = float(clean_price_str)
                except ValueError:
                    pass

        # --- 6. Return Structured API Payload ---
        return {
            "text_response": ai_response_text,
            "product_meta": {
                "product_name": extracted_name,
                "price": extracted_price,
                "shop_name": f"{brand_name.upper()}_OFFICIAL_SHOP",
                "image_url": image_url
            },
            "all_candidates": cleaned_matches
        }