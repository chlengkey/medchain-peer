from Chaincrypto import Crypto

class Record():

	patient_id = ""
	patient = ""
	anamnesis = ""
	
	def __init__(self, id="", patient="", anamnesis="", data=False):
		self.patient_id = id
		self.patient = patient
		self.anamnesis = anamnesis

		if data:
			self.patient_id = list(data.keys())[0]
			self.patient = Patient(data[self.patient_id]['patient'])
			self.anamnesis = Anamnesis(data[self.patient_id]['anamnesis'])

	def get(self):
		patient = self.patient.get()
		anamnesis = self.anamnesis.get()

		return {
			"{}".format(self.patient_id) : {
				"patient" : patient,
				"anamnesis" : anamnesis
			}
		}

class Anamnesis(Crypto):
	complaint = None
	diagnosis = None
	drugs = []
	doctor = None
	facility = None

	def __init__(self, anamnesis=False):
		self.complaint = None
		self.diagnosis = None
		self.drugs = []
		self.doctor = None
		self.facility = None

		if anamnesis:
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
	
	def set(self, id="", name="", gender="", weight="", height="", blood_pressure="", allergy=""):
		self.id = id
		self.name = name
		self.gender = gender
		self.weight = weight
		self.height = height
		self.allergy = allergy
		return self