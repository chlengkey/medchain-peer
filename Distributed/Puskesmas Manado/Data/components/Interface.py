from flask_restful import Resource, request
from .Controller import Controller
import os

class Interface(Resource):

	controller = Controller()

	def get(self, id=False):
		if id:
			return self.controller.get(id)
		return self.controller.list()
		
	def post(self):
		data = request.get_json()
		return self.controller.add(data)
		