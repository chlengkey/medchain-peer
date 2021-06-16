from .components.TokenController import TokenController
from .components.Generator import Generator

DEFAULT_TOKEN_PATH = "Token/store"

routes = [
	{
		"path" : "/token/check/<string:id>",
		"endpoint" : "tokenGetter",
		"component" : TokenController(DEFAULT_TOKEN_PATH)
	},
	{
		"path" : "/token/generate",
		"endpoint" : "tokenGenerate",
		"component" : Generator(DEFAULT_TOKEN_PATH)
	}
]

def register(api):
	for route in routes:
		api.add_resource(route["component"], route['path'], endpoint=route['endpoint'])