# 🛍️ AI Shopping Concierge — Enterprise RAG Commerce Platform

Aplikasi *Conversational Commerce* berbasis **Retrieval-Augmented Generation (RAG)** untuk rekomendasi dan transaksi peralatan *outdoor*. Platform ini menggabungkan model **Google Gemini 2.0**, penelusuran vektor semantik, klasterisasi niat pengguna (*NLU CNN 1D*), keranjang belanja interaktif (*multi-item cart*), serta kalkulasi checkout finansial presisi.

---

## 🔄 Diagram Alir System & Architecture Flow

Diagram di bawah ini menjelaskan alur kerja sistem dari saat pengguna memasukkan kueri hingga proses transaksi selesai:

flowchart TD
    A[User Input / Query] --> B{Entry Point}
    B -->|Streamlit UI| C[app.py]
    B -->|REST API| D[main.py / FastAPI]

    C --> E[AIConciergePipeline]
    D --> E

    subgraph NLU & Retrieval Engine
        E --> F["Intent Classifier / CNN 1D"]
        F --> G[Query Parser & Text Processing]
        G --> H["Semantic Search / Vector DB"]
        H --> I["product_vectors.pkl / Supabase"]
    end

    I -->|Retrieved Ground Truth| J[Grounded Context Payload]

    subgraph LLM Generation & Parsing
        J --> K[Gemini LLM Client]
        K --> L["Gemini 2.0 Flash / Lite"]
        L --> M[JSON Structured Output Parser]
    end

    M --> N[Product Recommendation Cards]
    N --> O[Add to Cart Action]

    subgraph Checkout & Payment Gateway
        O --> P[Multi-Item Cart Session State]
        P --> Q[SymPy Financial Calculator]
        Q --> R["Payment Settlement: QRIS / VA / E-Wallet"]
        R --> S[Transaction Log & Analytics]
    end
