from .components.TokenController import TokenController
from .components.Generator import Generator
from Router import Router

DEFAULT_TOKEN_PATH = "Token/store"

router = Router()
routes = [
	{
		"path" : "token",
		"children" : [
			{
				"path" : "create",
				"endpoint" : "TokenCreate",
				"component" : Generator,
				"payload" : {
					"path" : DEFAULT_TOKEN_PATH
				}
			},
			{
				"path" : "<string:id>",
				"endpoint" : "TokenGet",
				"component" : TokenController,
				"payload" : {
					"path" : DEFAULT_TOKEN_PATH
				}
			}
		]
	}
]

def register(api):
	router.register(api, routes)