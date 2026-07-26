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



'''''''''''''''''''''''''''''''''''''''''''''''''
| Modul & Teknologi | Stack / Teknologi | Fungsi |
| :--- | :--- | :--- |
| **Frontend UI** | Streamlit | Antarmuka obrolan dan panel checkout |
| **Backend API** | FastAPI / Uvicorn | Endpoint REST API untuk integrasi sistem eksternal |
| **Generative AI** | Google GenAI SDK (`gemini-2.0-flash-lite`) | Inferensi rekomendasi terstruktur |
| **NLU Engine** | TensorFlow / Keras (CNN 1D) | Klasifikasi niat pencarian kueri |
| **Database** | Supabase (PostgreSQL + pgvector) | Penyimpanan data relational dan vektor |
| **Validation Engine** | SymPy | Kalkulasi formula total tagihan transaksi |
