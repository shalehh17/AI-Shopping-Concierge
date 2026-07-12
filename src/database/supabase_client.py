import os
from dotenv import load_dotenv
from supabase import create_client, Client

# 1. Muat variabel lingkungan dari file .env secara otomatis
load_dotenv()

# 2. Ambil kredensial dari environment variable 
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY")

# 3. Validasi keberadaan kredensial untuk mencegah error koneksi kosong
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Error: Kredensial SUPABASE_URL atau SUPABASE_PUBLISHABLE_KEY tidak ditemukan di file .env!")

# 4. Inisialisasi object client Supabase yang siap digunakan di file lain
try:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("Koneksi client ke database Supabase berhasil diinisialisasi.")
except Exception as e:
    print(f"Gagal menginisialisasi client Supabase: {str(e)}")