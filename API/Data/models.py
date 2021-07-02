from Chaincrypto import Crypto
from datetime import datetime

class Record():

	patient_id = ""
	patient = ""
	anamnesis = ""
	
	def __init__(self, id="", patient="", anamnesis="", data=False):
		self.patient_id = id
		self.patient = patient
		self.anamnesis = anamnesis
		self.tanggal = str(datetime.now())

		if data:
			self.patient_id = list(data.keys())[0]
			self.tanggal = str(datetime.now())
			self.patient = Patient(data[self.patient_id]['patient'])
			self.anamnesis = Anamnesis(data[self.patient_id]['anamnesis'])

	def get(self):
		app = self
		patient = self.patient.get()
		anamnesis = self.anamnesis.get()

		return {
			"{}".format(self.patient_id) : {
				"patient" : patient,
				"anamnesis" : anamnesis,
				"tanggal" : app.tanggal
			}
		}

class Anamnesis(Crypto):

	def __init__(self, anamnesis=False):
		self.complaint = None
		self.diagnosis = None
		self.drugs = []
		self.doctor = None
		self.facility = None

		if anamnesis:
			if "date_time" not in anamnesis or anamnesis['date_time'] == None:
				anamnesis['date_time'] = str(datetime.now())
			self.__dict__ = anamnesis

	def set(self, complaint="", diagnosis="", drugs="", doctor="", facility=""):
		self.complaint = complaint
		self.diagnosis = diagnosis
		self.drugs = drugs
		self.doctor = doctor
		self.facility = facility
		return self

class Patient(Crypto):
	id = None
	name = None
	borndate = None
	gender = None
	weight = None
	height = None
	blood_type = None
	allergy = {
		"drugs" : [],
		"food" : []
	}

	def __init__(self, patient=False):
		self.id = None
		self.name = None
		self.borndate = None
		self.gender = None
		self.weight = None
		self.height = None
		self.blood_type = None
		self.allergy = {
			"drugs" : [],
			"food" : []
		}
		if patient:
			self.__dict__ = patient
	
	def set(self, id="", name="", gender="", weight="", height="", blood_type="", allergy=""):
		self.id = id
		self.name = name
		self.gender = gender
		self.weight = weight
		self.height = height
		self.allergy = allergy
		return self