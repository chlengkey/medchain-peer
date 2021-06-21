from flask_restful import Resource,request
from flask import request, abort
from Blockchain import Chain
from Data.models import Patient, Anamnesis
from Chaincrypto import KeyBinding, Processor
import random, shutil, time, os, json

class TokenController(Resource):
	"""docstring for ClassName"""

	DEFAULT_TOKEN_PATH = None
	DEFAULT_BLOCKCHAIN_PATH = "Blockchain/store/mined"
	ERROR = {}

	def __init__(self, **kwargs):
		self.DEFAULT_TOKEN_PATH = kwargs['path']

	def get(self, id=None, check=False):
		if request.remote_addr != '127.0.0.1':
			abort(403)
			return False

		if not check:
			return self.tokenGetter(id)
		elif check:
			return self.tokenValid(id)

	def delete(self, id):
		if os.path.isdir(path):
			shutil.rmtree(path)
			return True
		return False

	def tokenValid(self, id):
		path = os.path.join(self.DEFAULT_TOKEN_PATH, id)
		if not os.path.exists(path):
			self.ERROR['code'] = "TOKEN_INVALID"
			self.ERROR['msg'] = "Token is not valid"
			self.ERROR['success'] = False
			return self.ERROR
		self.ERROR['code'] = "TOKEN_VALID"
		self.ERROR['msg'] = "Token is valid"
		self.ERROR['success'] = True
		return self.ERROR

	def tokenGetter(self, id):

		# Cek Jika Panjang Token adalah 5 Karakter
		if len(str(id)) < 5:
			self.ERROR['code'] = "TOKEN_LENGTH_MINIMAL_5_CHARACTER"
			self.ERROR['msg'] = "Token length should at least 4 character"
			self.ERROR['success'] = False
			return self.ERROR

		# Mencari directory Token
		path = os.path.join(self.DEFAULT_TOKEN_PATH, id)
		
		if not os.path.exists(path):
			self.ERROR['code'] = "TOKEN_INVALID"
			self.ERROR['msg'] = "Token is not valid"
			self.ERROR['success'] = False
			return self.ERROR

		# Membuka file token
		patientData = json.loads(self.openToken(path + "/data.json"))
		patient = Patient().set(patientData['id'], patientData['name'])

		# Decrypt Patient Private and Public Key
		key = KeyBinding("Chaincrypto/store")
		processor = Processor()
		patientPrivKey = self.openToken(path + "/credential.txt")
		patientPrivKey = processor.decrypt(key.getPrivateKey(), patientPrivKey)
		patientPublicKey = patientData['publicKey']

		# Mengambil data dari blockchain
		chain, valid = Chain().load(self.DEFAULT_BLOCKCHAIN_PATH)
		recordData = []

		for block in chain.extract()[1:]:
			for data in block.data:
				if patient.id in data.keys():
					record_data = data[patient.id]
					record_patient_data = Patient(record_data['patient']).decode(patientPrivKey)
					record_anamnesis_data = Anamnesis(record_data['anamnesis']).decode(patientPrivKey)
					
					recordData.append({
						"patient" : record_patient_data.get(), 
						"anamnesis" : record_anamnesis_data.get()
					})

		# Jika data record sudah pernah ada
		# Ambil data pasien yang memuat keadaan terakhir pasien
		if len(recordData) > 0:
			patient = Patient(recordData[len(recordData) - 1]['patient'])

		tokenValid = {
			'success' : True,
			'valid' : os.path.exists(path),
			'publicKey' : patientPublicKey,
			'patient' : patient.get(),
			'record' : recordData
		}

		#if os.path.exists(path):
		#	shutil.rmtree(path)

		return tokenValid

	def openToken(self, path):
		with open(path, "r") as file:
			loaded_json = file.read()
			return loaded_json