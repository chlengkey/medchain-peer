# Daftar Pertanyaan dan Jawaban di API

### Dimana letak private dan public key puskesmas? 
Ada di Chaincrypto/store, terdapat dua file masing-masing 
private.pem : Memuat data private key
public.pem  : Memuat data public key

### Kenapa dipisah, public key dan private key dari puskesmas dipisah?
Supaya mempermudah pemanggilan data, karena ada kalanya private key digunakan sendiri 
dan public key digunakan sendiri

### File mana yang menunjukan pengaturan (Pembuatan dan Mining) Blockchain?
Terdapat pada folder Blockchain/components

### Dimana block dari blockchain disimpan?
Terdapat pada folder Blockchain/store, adapun blockchain terdiri dari 3 folder utama yaitu :
mined    : Memuat blockchain yang telah valid, dan telah dilakukan mining
pending  : Memuat data-data yang akan disusun dalam block baru nanti
rejected : Memuat block-block yang ditolak setelah dibuat

Khusus untuk rejected, ada kalanya pembuatan block tidak sesuai dengan standar yang telah ditentukan, sehingga dengan menggunakan
rejected, dapat menyimpan block-block yang rusak : 
Contoh Kasus
- Hash dari block berbeda dengan hash dari isi block
- Block ditambah dengan tidak dilakukan mining terlebih dahulu

