from .components.KeyBinding import KeyBinding
from .components.Processor import Processor
import json

class Crypto:

	def encode(self, cryptoKey=False):
		"""Mengencode data dictionary kelas menjadi Ciphertext"""

		key = KeyBinding()
		processor = Processor()
		cryptoKey = cryptoKey if cryptoKey else key.getPublicKey()
		encoded = processor.encrypt(cryptoKey, str(json.dumps(self.__dict__)))
		self.__dict__ = {'encoded': encoded}

		return self

	def decode(self, cryptoKey=False):
		"""Mengdecode data dictionary kelas menjadi Plaintext"""

		key = KeyBinding()
		processor = Processor()
		cryptoKey = cryptoKey if cryptoKey else key.getPrivateKey()
		decoded = processor.decrypt(cryptoKey, self.__dict__['encoded'])
		self.__dict__ = json.loads(decoded)

		return self

	def get(self):
		return self.__dict__

	def toJson(self):
		return json.dumps(self.__dict__)