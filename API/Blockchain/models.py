from Chaincrypto import Crypto
import json

class MedicalRecord(Crypto):
	pass

class Anamnesis(Crypto):
	complaint = None
	diagnosis = None
	drugs = []

	def __init__(self, anamnesis=False):
		self.complaint = None
		self.diagnosis = None
		self.drugs = []

		if anamnesis:
			self.__dict__ = anamnesis

class Patient(Crypto):
	id = None
	name = None
	gender = None
	weight = None
	height = None
	blood_pressure = None
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
		self.blood_pressure = None
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
		self.blood_pressure = blood_pressure
		self.allergy = allergy
		return self