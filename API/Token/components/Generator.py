from flask_restful import Resource,request
from controller.medichainRSA import medichainRSA
from ..models import Token
import os

class Generator(Resource):

	DEFAULT_TOKEN_PATH = ""

	def __init__(self, DEFAULT_TOKEN_PATH):
		self.DEFAULT_TOKEN_PATH = DEFAULT_TOKEN_PATH

	def post(self, encryptedPrivateKey="12345"):

		data = request.get_json()
		RSAInstance = medichainRSA()
		
		if 'payload' not in data:
			return {"msg" : "Error!, payload tidak dapat ditemukan, anda harus menyertakan payload"}
		
		try:

			token = Token()

			# Menyetting agar path menuju ke /local/token/{nomor_token}
			path_to_token = "{}/{}".format(self.DEFAULT_TOKEN_PATH, token.__dict__['token'])
			path = os.path.join(os.getcwd(), path_to_token)

			# Membuat folder dengan nomor token
			os.mkdir(path)

			# Private key yang terenkripsi menggunakan public key fasilitas kesehatan
			file_out = open(path + "/credential.txt", "wb")
			file_out.write(bytes(data['payload'], 'utf-8'))
			file_out.close()

			# Menyimpan waktu expire dari token
			file_out = open(str(path + "/{}".format(token.__dict__['expire'])), "wb")
			file_out.write(b"timestamp")
			file_out.close()

			return token

		except Exception as e:
			return e 
		