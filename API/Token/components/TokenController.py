from flask_restful import Resource,request
from flask import request, abort
from Blockchain import Chain
from Data.models import Patient, Anamnesis
import random, shutil, time, os, json

class TokenController(Resource):
	"""docstring for ClassName"""

	DEFAULT_TOKEN_PATH = None
	DEFAULT_BLOCKCHAIN_PATH = "Blockchain/store/mined"
	ERROR = {}

	def __init__(self, **kwargs):
		self.DEFAULT_TOKEN_PATH = kwargs['path']

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
			self.ERROR['code'] = "TOKEN_LENGTH_MINIMAL_5_CHARACTER"
			self.ERROR['msg'] = "Token length should at least 4 character"
			return self.ERROR

		# Mencari directory Token
		path = os.path.join(self.DEFAULT_TOKEN_PATH, id)
		
		# Membuka file token
		patientData = json.loads(self.openToken(path + "/data.json"))
		patient = Patient().set(patientData['id'], patientData['name'])
		
		patientPrivKey = self.openToken(path + "/credential.txt")
		
		# Mengambil data dari blockchain
		chain, valid = Chain().load(self.DEFAULT_BLOCKCHAIN_PATH)
		recordData = []

		for block in chain.extract()[1:]:
			for data in block.data:
				if patient.id in data.keys():
					record_data = data[patient.id]
					record_patient_data = Patient(record_data['patient']).decode()
					record_anamnesis_data = Anamnesis(record_data['anamnesis']).decode()
					recordData.append({
						"patient" : record_patient_data.get(), 
						"anamnesis" : record_anamnesis_data.get()
					})

		tokenValid = {
			'valid' : os.path.exists(path)
		}

		#if os.path.exists(path):
		#	shutil.rmtree(path)

		return recordData

	def openToken(self, path):
		with open(path, "r") as file:
			loaded_json = file.read()
			return loaded_json