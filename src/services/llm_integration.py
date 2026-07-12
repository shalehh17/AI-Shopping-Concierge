from google import genai
from src.config import Config

class GeminiLLMClient:
    def __init__(self):
        """
        Model Client Initialization (RAG Architecture).
        Instantiates the Generative AI inference client for production workflows, 
        leveraging modern SDK architecture for maximum compatibility and stateless execution.
        """
        # Credential Validation Layer: Pre-flight check to prevent runtime authentication failures
        if not Config.GEMINI_API_KEY:
            raise ValueError("[Configuration Error] GEMINI_API_KEY is missing from the environment runtime.")
            
        # SDK Client Instantiation: Establish secure connection to Generative LLM endpoint
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        
        # Dependency Resolution: Define foundational model identifier for deterministic routing
        self.model_name = "gemini-2.5-flash"

    def synthesize_shopping_recommendation(self, user_query: str, grounded_context: list) -> str:
        """
        Generative Inference Pipeline (Retrieval-Augmented Generation).
        Synthesizes structured retrieval payloads into natural language, strictly governed 
        by deterministic business logic and factual grounding constraints.
        """
        # Search Space Collapse Mitigation: Implement graceful degradation for null candidate sets
        if not grounded_context:
            return "Informasi stok tidak tersedia untuk kriteria produk yang diminta."

        # 1. Context Injection & Semantic Serialization
        # Serialize database records into unified textual representations to ensure factual consistency
        product_context_str = ""
        for idx, item in enumerate(grounded_context, 1):
            # Polymorphic Schema Resolution: Handle variations between raw ingestion and sanitized keys
            nama = item.get("Nama Produk", item.get("nama_produk", "Produk Tanpa Nama"))
            harga = item.get("Harga (Untuk Filter Metadata)", item.get("harga", 0))
            brand = item.get("Brand", item.get("brand", "-"))
            deskripsi = item.get("Deskripsi Teks (Untuk Embeddings)", item.get("deskripsi", ""))
            url = item.get("URL Produk (Tautan Pembelian)", item.get("url", "#"))
            
            product_context_str += (
                f"[{idx}] {nama}\n"
                f"    Brand: {brand}\n"
                f"    Harga: Rp {harga:,}\n"
                f"    Deskripsi: {deskripsi}\n"
                f"    Link Pembelian: {url}\n"
                f"{'-'*40}\n"
            )

        # 2. Unified Payload Orchestration (Deterministic Instruction Inlining)
        # Consolidate operational constraints and retrieval context into an atomic payload
        # to minimize hallucination risks and enforce strict data fidelity.
        prompt_payload = (
            "SISTEM INSTRUKSI (DETERMINISTIC CONSTRAINTS):\n"
            "Peran: AI Shopping Concierge profesional.\n"
            "Tugas: Merekomendasikan produk PALING RELEVAN dari daftar GROUND TRUTH di bawah.\n"
            "Constraint: Gunakan informasi Brand, Deskripsi, dan Link Pembelian secara presisi.\n"
            "Zero Hallucination Tolerance: Dilarang mengarang produk, memodifikasi spesifikasi, atau manipulasi harga!\n\n"
            f"--- DAFTAR PRODUK VALID (GROUND TRUTH) ---\n{product_context_str}\n"
            f"Kueri Pelanggan: '{user_query}'\n\n"
            "Respons Rekomendasi:"
        )

        # 3. Stateless LLM Inference Execution
        try:
            # Atomic Inference Cycle: Transmit payload to LLM endpoint for generative synthesis
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt_payload
            )
            return response.text
            
        except Exception as e:
            # Pipeline Monitoring: Log generation faults to maintain system observability
            return f"[Inference Pipeline Error] Generasi teks gagal: {str(e)}"