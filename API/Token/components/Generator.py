from flask_restful import Resource,request
from ..models import Token
import os, json

class Generator(Resource):

	DEFAULT_TOKEN_PATH = False
	ERROR = {
		"msg" : "Error!, payload can't be found",
		"code" : "PAYLOAD404"
	}

	def __init__(self, **kwargs):
		self.DEFAULT_TOKEN_PATH = kwargs['path']

	def post(self, encryptedPrivateKey=""):

		data = request.get_json()

		if "payload" not in data: 
			return self.ERROR
	
		try:

			# Membuat instance token baru
			token = Token()
			
			# Menyetting agar path menuju ke /local/token/{nomor_token}
			path_to_token = os.path.join(self.DEFAULT_TOKEN_PATH, token.get('token')) 
			path = os.path.join(os.getcwd(), path_to_token)

			# Membuat folder dengan nomor token
			os.mkdir(path)

			# Private key yang terenkripsi menggunakan public key fasilitas kesehatan
			file_out = open(os.path.join(path, "credential.txt"), "wb")
			file_out.write(bytes(data['payload'], 'utf-8'))
			file_out.close()

			# Private key yang terenkripsi menggunakan public key fasilitas kesehatan
			with open(os.path.join(path, "data.json"), "w") as file:
				json.dump(data['patient'], file)
				file.close()

			# Menyimpan waktu expire dari token
			file_out = open(os.path.join(path, str(token.get("expire"))), "wb")
			file_out.write(b"timestamp")
			file_out.close()
			
			return token.get()

		except Exception as e:
			self.ERROR['msg'] = str(e)
			self.ERROR['code'] = "TOKEN_ERROR"
			return self.ERROR
		