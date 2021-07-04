from .components.Interface import Interface
from .components.PatientInterface import PatientInterface
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
			},
			{
				"path" : "patient/raw/<string:id>",
				"endpoint" : "PatientRawData",
				"component" : PatientInterface()
			}
		]
	}
]

def register(api):
	router.register(api, routes)