from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast, base64, os

class KeyBinding():
	DEFAULT_KEY_PATH = "Chaincrypto/store"
	privateKey = ""
	publicKey = ""

	def __init__(self, path=""):
		
		if path == "":
			path = os.path.join(os.getcwd(), self.DEFAULT_KEY_PATH)

		# Mengambil Private Key dari file private.pem
		f = open(os.path.join(path, "private.pem"))
		self.privateKey = f.read();
		self.privateKey = """{}""".format(self.privateKey)

		# Mengambil Public Key dari file public.pem
		f = open(os.path.join(path, "public.pem"))
		self.publicKey  = f.read();
		self.publicKey = """{}""".format(self.publicKey)

	def getPrivateKey(self):
		return self.privateKey

	def getPublicKey(self):
		return self.publicKey