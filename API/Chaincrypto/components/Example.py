from KeyBinding import KeyBinding
from Processor import Processor

# Mengambil Key dari Chaincrypto/store
# Letakan pasangan key private dan public di path Chaincrypto/store
# private key dengan format private.pem
# public key dengan format public.pem
key = KeyBinding("../store")

# Menyiapkan Processor Enkripsi dan Dekripsi
processor = Processor()

# Melakukan Enkripsi
ciphertext = processor.encrypt(key.getPublicKey(), "tesData")
print("Ciphertext : ", ciphertext)

# Melakukan Dekripsi
plaintext = processor.decrypt(key.getPrivateKey(), ciphertext)
print("Plaintext : ", plaintext)