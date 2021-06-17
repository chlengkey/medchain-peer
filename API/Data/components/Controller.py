from ..models import Patient, Anamnesis, Record
import json, random
import os

class Controller():

	DEFAULT_PATH_TO_PENDING_BLOCK = "Blockchain/store/pending"

	def add(self, data):
		"""	Data akan ditambahkan ke folder pending sebelum dibuat menjadi satu blok utuh 
			Data terdiri dari 2 class yaitu : Patient, Anamnesis"""

		patient = Patient(data['patient']).encode()
		anamnesis = Anamnesis(data['anamnesis']).encode()
		record = Record(data['patient']['id'], patient, anamnesis)

		filename = "{}.json".format(str(random.randint(10000,99999)))
		filepath = os.path.join(os.getcwd(), self.DEFAULT_PATH_TO_PENDING_BLOCK, filename)
		with open(filepath, 'w') as outfile:
			json.dump(record.get(), outfile)
			outfile.close()

		return record.get()

	def get(self, id):
		""" Mengambil data berdasarkan ID yang ada """

		filename = str(id)
		if not id.endswith(".json"):
			filename += ".json"

		filepath = os.path.join(os.getcwd(), self.DEFAULT_PATH_TO_PENDING_BLOCK, filename)

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
		filepath = os.path.join(os.getcwd(), self.DEFAULT_PATH_TO_PENDING_BLOCK)
		
		for filename in os.listdir(filepath):
			filelist.append(self.get(filename))

		return filelist