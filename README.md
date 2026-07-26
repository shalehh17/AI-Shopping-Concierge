# 🛍️ AI Shopping Concierge — Enterprise RAG Commerce Platform

Aplikasi *Conversational Commerce* berbasis **Retrieval-Augmented Generation (RAG)** untuk rekomendasi dan transaksi peralatan *outdoor*. Platform ini menggabungkan model **Google Gemini 2.0**, penelusuran vektor semantik, klasterisasi niat pengguna (*NLU CNN 1D*), keranjang belanja interaktif (*multi-item cart*), serta kalkulasi checkout finansial presisi.

---
## 🔄 Diagram Alir System & Architecture Flow
Diagram di bawah ini menjelaskan alur kerja sistem dari saat pengguna memasukkan kueri hingga proses transaksi selesai:

<img width="1429" height="8192" alt="image" src="https://github.com/user-attachments/assets/18f3c6c6-4332-40ac-9a59-87bf29e46e29" />


## 🌟 Fitur Utama Platform
Semantic Product Search: Menerjemahkan kueri bebas pelanggan menjadi pencarian produk berbasis vektor.
NLU Intent Classification (CNN 1D): Mengklasifikasikan niat pencarian kueri secara otomatis dengan pemantauan performa real-time.
Deterministic JSON Output: Menjamin respons LLM bebas halusinasi dengan membatasi rekomendasi murni pada data ground truth.
Interactive Multi-Item Cart: Menampung banyak produk sekaligus, menghitung subtotal per item, dan memperbarui tampilan keranjang secara real-time.
SymPy Validated Checkout: Melakukan validasi matematis untuk kalkulasi harga barang, kuantitas, dan ongkos kirim.
Multi-Payment Gateway Simulation: Mendukung pembayaran via QRIS Dinamis, Virtual Account, dan E-Wallet.



```text
AI-Shopping-Concierge/
├── data/
│   ├── embeddings/
│   │   └── product_vectors.pkl
│   ├── processed/
│   │   └── cleaned_dataset.csv
│   └── raw/
│       └── Dataset_ecommerce_500.csv
├── docs/
│   ├── arsititektur_gambar/
│   │   └── Arsitektur_CNN1D_AI_Concierge.png
│   └── PPT Case Study ML.pdf
├── notebooks/
│   ├── 01_eda_and_preprocessing.ipynb
│   ├── 02_cnn_model_training_ipynb.ipynb
│   └── 03_vector_embeddings.ipynb
├── scripts/
│   └── AI_Shopping_Concierge_New.ipynb
├── src/
│   ├── database/
│   │   ├── __init__.py
│   │   ├── relational_queries.py
│   │   ├── supabase_client.py
│   │   └── vector_db_client.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── intent_classification_model.keras
│   │   ├── intent_classifier.py
│   │   └── semantic_search.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── concierge_pipeline.py
│   │   └── llm_integration.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── query_parser.py
│   │   └── scientific_calculator.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── text_processing.py
│   ├── __init__.py
│   ├── config.py
│   └── main.py
├── .gitignore
├── Procfile
├── README.md
├── app.py
├── logo.png
├── main.py
└── requirements.txt

<table border="1" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f6f8fa;">
      <th style="padding: 10px; text-align: left;">Modul & Teknologi</th>
      <th style="padding: 10px; text-align: left;">Stack / Teknologi</th>
      <th style="padding: 10px; text-align: left;">Fungsi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px;"><strong>Frontend UI</strong></td>
      <td style="padding: 8px;">Streamlit</td>
      <td style="padding: 8px;">Antarmuka obrolan dan panel checkout</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Backend API</strong></td>
      <td style="padding: 8px;">FastAPI / Uvicorn</td>
      <td style="padding: 8px;">Endpoint REST API untuk integrasi sistem eksternal</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Generative AI</strong></td>
      <td style="padding: 8px;">Google GenAI SDK (<code>gemini-2.0-flash-lite</code>)</td>
      <td style="padding: 8px;">Inferensi rekomendasi terstruktur</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>NLU Engine</strong></td>
      <td style="padding: 8px;">TensorFlow / Keras (CNN 1D)</td>
      <td style="padding: 8px;">Klasifikasi niat pencarian kueri</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Database</strong></td>
      <td style="padding: 8px;">Supabase (PostgreSQL + pgvector)</td>
      <td style="padding: 8px;">Penyimpanan data relational dan vektor</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Validation Engine</strong></td>
      <td style="padding: 8px;">SymPy</td>
      <td style="padding: 8px;">Kalkulasi formula total tagihan transaksi</td>
    </tr>
  </tbody>
</table>
