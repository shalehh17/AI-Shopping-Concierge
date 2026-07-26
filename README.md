# 🛍️ AI Shopping Concierge — Enterprise RAG Commerce Platform

Aplikasi *Conversational Commerce* berbasis **Retrieval-Augmented Generation (RAG)** untuk rekomendasi dan transaksi peralatan *outdoor*. Platform ini menggabungkan model **Google Gemini 2.0**, penelusuran vektor semantik, klasterisasi niat pengguna (*NLU CNN 1D*), keranjang belanja interaktif (*multi-item cart*), serta kalkulasi checkout finansial presisi.

---

## 🔄 Diagram Alir System & Architecture Flow

Diagram di bawah ini menjelaskan alur kerja sistem dari saat pengguna memasukkan kueri hingga proses transaksi selesai:

```mermaid
flowchart TD
    A[User Input / Query] --> B{Entry Point}
    B -->|Streamlit UI| C[app.py]
    B -->|REST API| D[main.py/FastAPI]

    C --> E[AIConciergePipeline]
    D --> E

    subgraph NLU & Retrieval Engine
        E --> F[Intent Classifier/CNN 1D]
        F --> G[Query Parser&Text Processing]
        G --> H[Semantic Search/Vector DB]
        H -->|Fetch Embeddings| I[Supabase]
    end

    I -->|Retrieved Ground Truth| J[Grounded Context Payload]

    subgraph LLM Generation & Parsing
        J --> K[Gemini LLM Client]
        K -->|Google GenAI API v1beta| L[Gemini 2.0 Flash]
        L -->|JSON Structured Output| M[JSON Parser]
    end

    M --> N[Product Recommendation Cards]
    N --> O[Add to Cart Action]

    subgraph Checkout & Payment Gateway
        O --> P[Multi-Item Cart Session State]
        P --> Q[SymPy Financial Calculator]
        Q --> R[Payment Settlement: QRIS / VA / E-Wallet]
        R --> S[Transaction Log & Analytics]
    end


# AI Shopping Concierge

## 🌟 Fitur Utama Platform

1. **Semantic Product Search**: Menerjemahkan kueri bebas pelanggan menjadi pencarian produk berbasis vektor.
2. **NLU Intent Classification (CNN 1D)**: Mengklasifikasikan niat pencarian kueri secara otomatis dengan pemantauan performa *real-time*.
3. **Deterministic JSON Output**: Menjamin respons LLM bebas halusinasi dengan membatasi rekomendasi murni pada data *ground truth*.
4. **Interactive Multi-Item Cart**: Menampung banyak produk sekaligus, menghitung subtotal per item, dan memperbarui tampilan keranjang secara *real-time*.
5. **SymPy Validated Checkout**: Melakukan validasi matematis untuk kalkulasi harga barang, kuantitas, dan ongkos kirim.
6. **Multi-Payment Gateway Simulation**: Mendukung pembayaran via QRIS Dinamis, Virtual Account, dan E-Wallet.

---

## 📁 Struktur Direktori Proyek

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
