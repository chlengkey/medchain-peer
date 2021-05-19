from Crypto import Random
from Crypto.PublicKey import RSA
from flask_restful import Api, Resource
from flask_restful import request
from Crypto.Cipher import PKCS1_OAEP
import ast
import base64


def toBase64(string):
	return base64.b64encode(string)

priv_key_txt = """-----BEGIN RSA PRIVATE KEY-----\n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\nvr3pRBbnPh61VScwX3T7otddR3N9OD0=\n-----END RSA PRIVATE KEY-----"""

class Cryp(Resource):

	privateKey = ""
	publicKey  = ""

	def post(self, id=None):

		# Get encrypted data
		data = request.get_json()

		# Decryptor
		decrypted = self.decrypt(priv_key_txt, data['publicKey'])
		encrypted = self.encrypt(decrypted, "sayang olek");

		return { 'io' : encrypted};
	
	# Menggunakan private key untuk dekripsi
	def decrypt(self, privateKey, stringData):
		# Membuat Private Key
		privateKey = RSA.importKey(privateKey)

		# Merubah dalam bentuk byte dan base64
		bytesData     = bytes(stringData ,'utf-8')
		base64Decoded = base64.b64decode(bytesData)

		# Memulai proses dekripsi
		decryptor = PKCS1_OAEP.new(privateKey)
		decrypted = decryptor.decrypt(ast.literal_eval(str(base64Decoded)))
		return str(decrypted.decode('utf-8'))

	# Menggunakan public key untuk enkripsi
	def encrypt(self, publicKey, stringData):
		# Membuat Public Key
		publicKey = RSA.importKey(publicKey)

		# Encryptor
		encryptor = PKCS1_OAEP.new(publicKey)
		encrypted = encryptor.encrypt(bytes(stringData, 'utf-8'))
		return str(toBase64(encrypted).decode('utf-8'))