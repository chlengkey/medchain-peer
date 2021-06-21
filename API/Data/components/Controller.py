from ..models import Patient, Anamnesis, Record
import json, random
import os

class Controller():

	DEFAULT_PATH_TO_PENDING_BLOCK = "Blockchain/store/pending"

	def add(self, data):
		"""	Data akan ditambahkan ke folder pending sebelum dibuat menjadi satu blok utuh 
			Data terdiri dari 2 class yaitu : Patient, Anamnesis"""

		# Mengambil data JSON
		patient_id = data['patient_id']
		patient = Patient(data['patient'])
		anamnesis = Anamnesis(data['anamnesis'])
		record = Record(patient_id, patient, anamnesis)

		filename = "{}.json".format(str(random.randint(10000,99999)))
		filepath = os.path.join(os.getcwd(), self.DEFAULT_PATH_TO_PENDING_BLOCK, filename)
		with open(filepath, 'w') as outfile:
			json.dump(record.get(), outfile)
			outfile.close()

		return {
			"msg" : "Success adding new data",
			"success" : True,
			"code" : "DATA200"
		}

	def get(self, id):
		""" Mengambil data berdasarkan ID yang ada """

		filename = str(id)
		if not id.endswith(".json"):
			filename += ".json"

		filepath = os.path.join(self.DEFAULT_PATH_TO_PENDING_BLOCK, filename)

		if os.path.exists(filepath):
			with open(filepath, 'r') as infile:
				loaded_json = json.loads(infile.read())
				infile.close()
				return Record(data=loaded_json).get()

		return {
			"msg" : "Can't find the corresponding data",
			"code" : "DATA404"
		}

	def list(self):
		""" Mengambil keseluruhan data """
		filelist = []
		filepath = os.path.join(self.DEFAULT_PATH_TO_PENDING_BLOCK)
		
		for filename in os.listdir(filepath):
			filelist.append(self.get(filename))

		return filelist