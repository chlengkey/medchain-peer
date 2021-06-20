from .components.KeyBinding import KeyBinding
from .components.Processor import Processor
import json

class Crypto:

	def encode(self, cryptoKey=False):
		"""Mengencode data dictionary kelas menjadi Ciphertext"""

		key = KeyBinding()
		processor = Processor()
		cryptoKey = cryptoKey if cryptoKey else key.getPublicKey()
		
		dataKeys = list(self.get().keys())
		for dataKey in dataKeys:
			if dataKey != "id":
				self.__dict__[dataKey] = processor.encrypt(cryptoKey, self.get()[dataKey])
		
		return self

	def decode(self, cryptoKey=False):
		"""Mengdecode data dictionary kelas menjadi Plaintext"""

		key = KeyBinding()
		processor = Processor()
		cryptoKey = cryptoKey if cryptoKey else key.getPrivateKey()

		dataKeys = list(self.get().keys())
		for dataKey in dataKeys:
			if dataKey != "id":
				self.__dict__[dataKey] = processor.decrypt(cryptoKey, self.__dict__[dataKey])

		return self

	def get(self):
		return self.__dict__

	def toJson(self):
		return json.dumps(self.__dict__)