from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def generateKey():
	key = RSA.generate(2048)
	private_key = key.export_key()
	file_out = open("private.pem", "wb")
	file_out.write(private_key)
	file_out.close()

	public_key = key.publickey().export_key()
	file_out = open("receiver.pem", "wb")
	file_out.write(public_key)
	file_out.close()

#generateKey()

def encryptMessage(data, path_to_public_key):
	data     = data.encode("utf-8")
	file_out = open("encrypted_data.bin", "wb")
	recipient_key = RSA.import_key(open(path_to_public_key).read())
	session_key = get_random_bytes(16)

	# Encrypt the session key with the public RSA key
	cipher_rsa = PKCS1_OAEP.new(recipient_key)
	enc_session_key = cipher_rsa.encrypt(session_key)

	# Encrypt the data with the AES session key
	cipher_aes = AES.new(session_key, AES.MODE_EAX)
	ciphertext, tag = cipher_aes.encrypt_and_digest(data)
	[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
	file_out.close()

def decryptMessage(path_to_bin, path_to_private_key):
	file_in = open(path_to_bin, "rb")
	private_key = RSA.import_key(open(path_to_private_key).read())
	enc_session_key, nonce, tag, ciphertext = \
	   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

	# Decrypt the session key with the private RSA key
	cipher_rsa = PKCS1_OAEP.new(private_key)
	session_key = cipher_rsa.decrypt(enc_session_key)

	# Decrypt the data with the AES session key
	cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
	data = cipher_aes.decrypt_and_verify(ciphertext, tag)
	print(data.decode("utf-8"))

encryptMessage("Lorem Ipsum adalah contoh teks atau dummy dalam industri percetakan dan penataan huruf atau typesetting. Lorem Ipsum telah menjadi standar contoh teks sejak tahun 1500an, saat seorang tukang cetak yang tidak dikenal mengambil sebuah kumpulan teks dan mengacaknya untuk menjadi sebuah buku contoh huruf. Ia tidak hanya bertahan selama 5 abad, tapi juga telah beralih ke penataan huruf elektronik, tanpa ada perubahan apapun. Ia mulai dipopulerkan pada tahun 1960 dengan diluncurkannya lembaran-lembaran Letraset yang menggunakan kalimat-kalimat dari Lorem Ipsum, dan seiring munculnya perangkat lunak Desktop Publishing seperti Aldus PageMaker juga memiliki versi Lorem Ipsum.", "receiver.pem")
decryptMessage("encrypted_data.bin", "private.pem")