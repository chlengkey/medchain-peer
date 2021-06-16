class Token():

	token = ""
	valid = ""
	expire = ""

	def __init__(self, token="", valid="", expire=""):
		self.token = str(random.randint(10000,99999))
		self.valid = True
		self.expire = time.time() + 3600

		if token != "":
			self.token = token
		if valid != "":
			self.valid = valid
		if expire != "":
			self.expire = expire