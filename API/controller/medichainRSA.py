from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast
import base64

def toBase64(string):
	return base64.b64encode(string)

class medichainRSA():

	privateKey = ""
	publicKey  = ""

	def __init__(self, privateKey="", publicKey=""):
		self.privateKey = privateKey
		self.publicKey  = publicKey

	# Menggunakan private key untuk dekripsi
	def decrypt(self, stringData):
		# Membuat Private Key
		privateKey = RSA.importKey(self.privateKey)

		# Merubah dalam bentuk byte dan base64
		bytesData     = bytes(stringData ,'utf-8')
		base64Decoded = base64.b64decode(bytesData)

		# Memulai proses dekripsi
		decryptor = PKCS1_OAEP.new(privateKey)
		decrypted = decryptor.decrypt(ast.literal_eval(str(base64Decoded)))
		return str(decrypted.decode('utf-8'))

	# Menggunakan public key untuk enkripsi
	def encrypt(self, stringData):
		# Membuat Public Key
		publicKey = RSA.importKey(self.publicKey)

		# Encryptor
		encryptor = PKCS1_OAEP.new(publicKey)
		encrypted = encryptor.encrypt(bytes(stringData, 'utf-8'))
		return str(toBase64(encrypted).decode('utf-8'))
		