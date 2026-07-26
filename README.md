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
        E --> F[IntentClassifier/CNN 1D]
        F --> G[QueryParser&Text Processing]
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
        Q --> R[Payment Settlement]
        R --> S[Transaction Log & Analytics]
    end
















AI Shopping Concierge
🌟 Fitur Utama Platform
Semantic Product Search: Menerjemahkan kueri bebas pelanggan menjadi pencarian produk berbasis vektor.

NLU Intent Classification (CNN 1D): Mengklasifikasikan niat pencarian kueri secara otomatis dengan pemantauan performa real-time.

Deterministic JSON Output: Menjamin respons LLM bebas halusinasi dengan membatasi rekomendasi murni pada data ground truth.

Interactive Multi-Item Cart: Menampung banyak produk sekaligus, menghitung subtotal per item, dan memperbarui tampilan keranjang secara real-time.

SymPy Validated Checkout: Melakukan validasi matematis untuk kalkulasi harga barang, kuantitas, dan ongkos kirim.

Multi-Payment Gateway Simulation: Mendukung pembayaran via QRIS Dinamis, Virtual Account, dan E-Wallet.


