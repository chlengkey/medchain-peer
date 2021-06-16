from .components.BlockController import BlockController
from Router import Router
import os

DEFAULT_MINED_BLOCK_PATH = "Blockchain/store/mined"
DEFAULT_REJECT_BLOCK_PATH = "Blockchain/store/rejected"
DEFAULT_PENDING_BLOCK_PATH = "Blockchain/store/pending"

router = Router()
routes = [
	{
		"path" : "block",
		"children" : [
			{
				"path" : "create",
				"component" : BlockController,
				"endpoint" : "CreateBlock",
				"payload" : {
					"path" : DEFAULT_PENDING_BLOCK_PATH
				}
			},
			{
				"path" : "<string:id>",
				"component" : BlockController,
				"endpoint" : "MinedBlock",
				"payload" : {
					'path' : DEFAULT_MINED_BLOCK_PATH
				}
			},
			{
				"path" : "rejected/<string:id>",
				"component" : BlockController,
				"endpoint" : "RejectedBlock",
				"payload" : {
					'path' : DEFAULT_REJECT_BLOCK_PATH
				}
			},
			{
				"path" : "pending/<string:id>",
				"component" : BlockController,
				"endpoint" : "PendingBlock",
				"payload" : {
					'path' : DEFAULT_PENDING_BLOCK_PATH
				}
			},
		]
	}
]

def register(api):
	router.register(api, routes)