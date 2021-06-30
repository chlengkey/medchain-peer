from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast, base64, os

def toBase64(string):
	return base64.b64encode(string)

class Processor():
	
	def encrypt(self, key="", string="", useDefaultKey=False):

		# Membuat Public Key
		publicKey = RSA.importKey(key)

		# Encryptor
		encryptor = PKCS1_OAEP.new(publicKey)
		encrypted = encryptor.encrypt(bytes(string, 'utf-8'))
		return str(toBase64(encrypted).decode('utf-8'))

	def decrypt(self, key="", string="", useDefaultKey=False):

		# Membuat Private Key
		privateKey = RSA.importKey(key)

		# Merubah dalam bentuk byte dan base64
		bytesData     = bytes(string ,'utf-8')
		base64Decoded = base64.b64decode(bytesData)

		# Memulai proses dekripsi
		decryptor = PKCS1_OAEP.new(privateKey)
		decrypted = decryptor.decrypt(ast.literal_eval(str(base64Decoded)))
		return str(decrypted.decode('utf-8'))