from flask_restful import Resource, request
from .Mining import Mining

class MiningInterface(Resource, Mining):

	def get(self):
		valid, message = self.get_pending_data()
		if not valid:
			return message
		ERROR = {"code" : "MINING_NEEDED", "msg" : "Mining dibutuhkan, silahkan lakukan mining"}
		return ERROR

	def post(self):
		mining = Mining()
		return mining.start()