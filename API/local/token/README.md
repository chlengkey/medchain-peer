
# Token Data
Daftar token yang terdaftar dapat ditemukan disini

### Detail
- Nomor token adalah folder dari dimana token dibuat
- Contoh, untuk token '33456' merupakan token untuk "John"
- Maka token dapat ditemukan di {host}/local/token/33456

### Struktur Data
Token Terdiri dari 2 file di dalam satu folder : credential.bin, {timestamp}
- credential.bin
  berisi private_key yang dimiliki oleh pasien yang telah dienkripsi menggunakan public_key fasilitas kesehatan
- {timestamp}
  file yang memuat waktu expire dari token, timestamp dapat bervariasi, contohnya 203232232321
