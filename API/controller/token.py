from flask_restful import Resource,request
from flask import request, abort
from controller.medichainRSA import medichainRSA
import random
import shutil
import time
import os
import json

class Token(Resource):
	"""docstring for ClassName"""

	def get(self, id=None):
		
		if request.remote_addr != '127.0.0.1':
			abort(403)
			return False
		
		return self.tokenGetter(id)

	def delete(self, id):
		if os.path.isdir(path):
			shutil.rmtree(path)
			return True
		return False

	def tokenGetter(self, id):

		# Check if token is at least 5 character
		if len(str(id)) < 5:
			return {
				'valid' : False,
				'msg'   : "Token length should be 5 character"
			}

		# Search for token path
		path_to_token = "local/token/{}".format(id)
		path = os.path.join(os.getcwd(), path_to_token)
		
		tokenValid = {
			'valid' : os.path.exists(path)
		}

		return tokenValid


class Generator(Resource):

	"""def get(self, id=None):
		token = Token()
		tokenValue = token.tokenGetter(id)
		
		# Generate new token if old token is not exist
		if not tokenValue['valid']:
			newToken =  {
				'token'  : str(random.randint(10000,99999)),
				'valid'  : True,
				'expire' :  
			}

			# Private key yang terenkripsi menggunakan public key fasilitas kesehatan
			privateKey = "blablabla"
			file_out = open("receiver.pem", "wb")
			file_out.write(public_key)
			file_out.close()

			return newToken

		return tokenValue"""

	def post(self, encryptedPrivateKey="12345"):

		data = request.get_json()
		RSAInstance = medichainRSA()

		if 'payload' not in data:
			return {"msg" : "Error!, payload tidak dapat ditemukan, anda harus menyertakan payload"}
		
		try:

			# Menggenerate token baru
			token = {
				'token'  : str(random.randint(10000,99999)),
				'valid'  : True,
				'expire' : time.time() + 3600
			}

			# Menyetting agar path menuju ke /local/token/{nomor_token}
			path_to_token = "local/token/{}".format(token['token'])
			path = os.path.join(os.getcwd(), path_to_token)

			# Membuat folder dengan nomor token
			os.mkdir(path)

			# Private key yang terenkripsi menggunakan public key fasilitas kesehatan
			file_out = open(path + "/credential.txt", "wb")
			file_out.write(bytes(data['payload'], 'utf-8'))
			file_out.close()

			# Menyimpan waktu expire dari token
			file_out = open(str(path + "/{}".format(token['expire'])), "wb")
			file_out.write(b"timestamp")
			file_out.close()

			return token

		except Exception as e:
			return e 
		