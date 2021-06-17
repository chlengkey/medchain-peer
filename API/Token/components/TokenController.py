from flask_restful import Resource,request
from flask import request, abort
import random, shutil, time, os, json

class TokenController(Resource):
	"""docstring for ClassName"""

	DEFAULT_TOKEN_PATH = None

	def __init__(self, DEFAULT_TOKEN_PATH):
		self.DEFAULT_TOKEN_PATH = DEFAULT_TOKEN_PATH

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

		# Cek Jika Panjang Token adalah 5 Karakter
		if len(str(id)) < 5:
			return {
				'valid' : False,
				'msg'   : "Token length should be 5 character"
			}

		# Mencari directory Token
		path_to_token = os.path.join(self.DEFAULT_TOKEN_PATH, id)
		path = os.path.join(os.getcwd(), path_to_token)
		
		tokenValid = {
			'valid' : os.path.exists(path)
		}

		if os.path.exists(path):
			shutil.rmtree(path)

		return tokenValid
