from flask_restful import Resource, request
from .Mining import Mining

class MiningInterface(Resource):

	def post(self):
		mining = Mining()
		return mining.start()