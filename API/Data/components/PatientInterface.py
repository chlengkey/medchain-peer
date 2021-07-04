from flask_restful import Resource, request
from .Controller import Controller
import os

class PatientInterface(Resource):

	def get(self, id=False):
		controller = Controller()
		return controller.get_patient_from_blockchain(id)
		