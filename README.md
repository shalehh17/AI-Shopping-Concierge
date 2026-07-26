# 🛍️ AI Shopping Concierge — Enterprise RAG Commerce Platform

Aplikasi *Conversational Commerce* berbasis **Retrieval-Augmented Generation (RAG)** untuk rekomendasi dan transaksi peralatan *outdoor*. Platform ini menggabungkan model **Google Gemini 2.0**, penelusuran vektor semantik, klasterisasi niat pengguna (*NLU CNN 1D*), keranjang belanja interaktif (*multi-item cart*), serta kalkulasi checkout finansial presisi.

---

<img width="1429" height="8192" alt="image" src="https://github.com/user-attachments/assets/18f3c6c6-4332-40ac-9a59-87bf29e46e29" />


## 🌟 Fitur Utama Platform
Semantic Product Search: Menerjemahkan kueri bebas pelanggan menjadi pencarian produk berbasis vektor.
NLU Intent Classification (CNN 1D): Mengklasifikasikan niat pencarian kueri secara otomatis dengan pemantauan performa real-time.
Deterministic JSON Output: Menjamin respons LLM bebas halusinasi dengan membatasi rekomendasi murni pada data ground truth.
Interactive Multi-Item Cart: Menampung banyak produk sekaligus, menghitung subtotal per item, dan memperbarui tampilan keranjang secara real-time.
SymPy Validated Checkout: Melakukan validasi matematis untuk kalkulasi harga barang, kuantitas, dan ongkos kirim.
Multi-Payment Gateway Simulation: Mendukung pembayaran via QRIS Dinamis, Virtual Account, dan E-Wallet.
