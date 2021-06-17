from .components.BlockInterface import BlockInterface
from .components.MiningInterface import MiningInterface
from Router import Router
import os

DEFAULT_MINED_BLOCK_PATH = "Blockchain/store/mined"
DEFAULT_REJECT_BLOCK_PATH = "Blockchain/store/rejected"
DEFAULT_PENDING_BLOCK_PATH = "Blockchain/store/pending"

if not os.path.exists(DEFAULT_MINED_BLOCK_PATH):
	os.mkdir(DEFAULT_MINED_BLOCK_PATH)

if not os.path.exists(DEFAULT_REJECT_BLOCK_PATH):
	os.mkdir(DEFAULT_REJECT_BLOCK_PATH)

if not os.path.exists(DEFAULT_PENDING_BLOCK_PATH):
	os.mkdir(DEFAULT_PENDING_BLOCK_PATH)

router = Router()
routes = [
	{
		"path" : "block",
		"children" : [
			{
				"path" : "create",
				"component" : BlockInterface,
				"endpoint" : "CreateBlock",
				"payload" : {
					"path" : DEFAULT_PENDING_BLOCK_PATH
				}
			},
			{
				"path" : "<string:id>",
				"component" : BlockInterface,
				"endpoint" : "MinedBlock",
				"payload" : {
					'path' : DEFAULT_MINED_BLOCK_PATH
				}
			},
			{
				"path" : "mine",
				"endpoint" : "BlockMining",
				"component" : MiningInterface
			}
		]
	}
]

def register(api):
	router.register(api, routes)