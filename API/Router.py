import os

class Router():
	def register(self, api, routes, parent="/"):
		for route in routes:
			path = ""
			if parent == "/":
				path = parent + route['path']
			else:
				path = parent + "/" + route['path']
			#path = os.path.join(parent, route['path'])
			if "children" in route:
				self.register(api, route['children'], parent=path)
			else:
				if "payload" in route:
					print(path)
					api.add_resource(route['component'], path, endpoint=route['endpoint'], resource_class_kwargs=route['payload'])
				else:
					api.add_resource(route['component'], path, endpoint=route['endpoint'])
			