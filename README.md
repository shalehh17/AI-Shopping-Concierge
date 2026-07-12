# 🛒 AI Shopping Concierge: End-to-End Smart E-Commerce Platform

An enterprise-grade AI Shopping Concierge application integrating a high-performance **FastAPI** backend endpoint with an interactive, production-ready **Streamlit** frontend interface. The architecture features an advanced Multi-Entity Extraction NLU powered by **Gemini API JSON Mode**, mapped against a **Supabase** backend utilizing Hybrid Search (Vector + Relational) to deliver optimal outdoor product recommendations.

---

## 🚀 Key Features & Architectural Capabilities

*   **Semantic NLU Engine (JSON Mode):** Migrated from keyword-based heuristic models to a robust entity parsing network leveraging *Gemini API Structured Output*. Captures casual conversational phrases, local slang, and typos in real-time to translate them into structured parameter payloads (`sub_category`, `max_price`, technical features).
*   **Unified RAG Architecture:** The parsed search parameters dynamically query the Supabase relational database (`execute_hybrid_retrieval`). The system seamlessly blends relational table filtering with semantic text vector similarity indices to accurately return the `top_k=3` most relevant items.
*   **Live Data Science Dashboard (Streamlit UI):** Integrates an active observability suite on the UI sidebar. Displays interactive execution metrics alongside real-time 1D CNN training Accuracy and Loss performance analytics that scale adaptively against token string counts.
*   **Persisted Commercial Loop & Mathematical Validation:** Features an interactive checkout mechanism where user variations are processed under a *SymPy Mathematical Engine* to prevent floating-point decimal precision errors, recording transactional data inside a persistent ledger alongside real-time payment mode analytics charts.

---

## 📈 Technical Data Framework

1.  **E-Commerce Catalog Data:** Structured relational records mapping item identifiers, descriptions, pricing matrices, sub-categories, official media resources, and brand fields.
2.  **Unstructured Linguistic Inputs:** Raw string logs extracted from user interactions, transformed dynamically into programmatic schemas.
3.  **Semantic Similarity Matrices:** High-dimensional dense vectors (`embeddings`) mapping semantic vector proximities aligned with operational CNN learning metrics.
4.  **Transaction & Payment Logs:** Relational databases documenting order volume, chosen product metrics, precise processing timestamps, and payment conduits (QRIS, Mobile Banking, E-Wallet).

---

## 📂 Project Structure

```text
FINAL PROJECT AI SHOPPING CONCIERGE/
├── .streamlit/
│   └── config.toml             # Streamlit Theme and Interface Config
├── data/
│   ├── embeddings/
│   │   └── product_vectors.pkl # Serialized Dense Vector Embeddings
│   ├── processed/
│   │   └── cleaned_dataset.csv # Cleaned Structural Product Catalog
│   └── raw/
│       └── Dataset_ecommerce_500.csv # Raw Structural Data Source
├── notebooks/
│   ├── 01_eda_and_preprocessing.ipynb
│   ├── 02_cnn_model_training_ipynb.ipynb
│   └── 03_vector_embeddings.ipynb
├── scripts/
│   ├── AI_Shopping_Concierge_New.ipynb
│   └── Arsitektur_Gambar/
├── src/
│   ├── __pycache__/
│   ├── models/
│   │   ├── intent_classification_model.keras # Saved CNN Weights
│   │   ├── intent_classifier.py
│   │   └── semantic_search.py
│   ├── services/
│   │   ├── concierge_pipeline.py  # Core RAG Architecture Coordination
│   │   ├── llm_integration.py     # Gemini NLU Extraction Pipelines
│   │   └── supabase_client.py     # Persistent Database Connectors
│   ├── tools/
│   │   ├── query_parser.py        # Token & Intent Processing Layer
│   │   └── scientific_calculator.py # SymPy Mathematical Engine
│   ├── utils/
│   │   └── text_processing.py
│   └── config.py                  # Core Application Environment Configuration
├── venv/                          # Local Environment Isolation Folder
├── .env                           # Protected API Credentials (Ignored by Git)
├── .gitignore                     # Secure Resource Exclusions File
├── app.py                         # Interactive Streamlit Application UI
├── logo.png                       # Asset Graphic Resource
├── main.py                        # FastAPI Backend Application Entrypoint
├── Procfile                       # Production Cloud Deployment Directives
├── pyvenv.cfg
└── requirements.txt               # Declared Python Package Dependencies

---

🛠️ Technology Stack
Web Services & API Core: FastAPI, Uvicorn
Interactive Interface: Streamlit
Storage & Vector Retrieval: Supabase (PostgreSQL with pgvector extensions)
AI Models & Processing: Google GenAI SDK (Gemini API), TensorFlow/Keras (1D CNN)
Mathematical Operations: SymPy Engine
Data Structures: Pandas, NumPy, SciPy

🔧 Installation & Verification
Clone & Target Directory:

Bash
git clone [https://github.com/shalehh17/AI-Shopping-Concierge.git](https://github.com/shalehh17/AI-Shopping-Concierge.git)
cd "Final Project AI SHOPPING CONCIERGE"

Initialize Environment & Dependencies:

Bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Establish Local Settings:
Configure a .env file in the main folder using your credential tokens:

Cuplikan kode
GEMINI_API_KEY=your_gemini_api_token
SUPABASE_URL=your_supabase_endpoint
SUPABASE_KEY=your_supabase_anon_or_service_key
Booting Application Modules:

Launch Production API Layer:

Bash
uvicorn main:app --reload --port 8000
Launch User Interface:

Bash
streamlit run app.py --server.port=8501
🌐 API Interaction & Deployment
The application logic exposes an interactive Swagger UI documentation console natively generated by FastAPI. When running locally or deployed via a cloud framework, navigate to the API route to perform runtime evaluations:

Interactive API Dashboard: http://127.0.0.1:8000/docs

Primary Recommendation Endpoint: POST /api/recommend


