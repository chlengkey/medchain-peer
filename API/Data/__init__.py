from .components.Interface import Interface
from Router import Router

router = Router()
routes = [
	{
		"path" : "data",
		"children" : [
			{
				"path" : "create",
				"endpoint" : "CreateNewPendingData",
				"component" : Interface()
			},
			{
				"path" : "<string:id>",
				"endpoint" : "GetPendingData",
				"component" : Interface()
			},
			{
				"path" : "",
				"endpoint" : "GetListData",
				"component" : Interface()
			}
		]
	}
]

def register(api):
	router.register(api, routes)