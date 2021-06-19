from flask_restful import Resource, request
from .Chain import Chain
import json

class ChainInterface(Resource):
	
	def get(self, id="110"):
		chain, valid = Chain().load("Blockchain/store/mined", blockToJson=True)
		if not id : 
			return chain.extract()
		for chain in chain.extract():
			print(chain)