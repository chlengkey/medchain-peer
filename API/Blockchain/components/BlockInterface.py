from flask_restful import Resource,request
from flask import request, abort
from .Block import Block
import os, json

class BlockInterface(Resource):
	
	DEFAULT_BLOCK_PATH = None
	BLOCK_NOT_FOUND = {
		"msg" : "Block is missing or not found!",
		"code" : "BLOCK404"
	}

	def __init__(self, **kwargs):
		if kwargs != {} : self.DEFAULT_BLOCK_PATH = kwargs['path']

	def get(self, id=""):
		path_to_block = os.path.join(self.DEFAULT_BLOCK_PATH, id + ".json")
		if not os.path.exists(path_to_block): 
			return self.BLOCK_NOT_FOUND

	def post(self, data=None):
		block = Block(1, "data")
		with open(os.path.join(os.getcwd(), self.DEFAULT_BLOCK_PATH, 'data.json'), 'w') as outfile:
			json.dump(block.__dict__, outfile)
		return "new block added"