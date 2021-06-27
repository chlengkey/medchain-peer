from .Block import Block
from .Chain import Chain
from Data.components.Controller import Controller
import shutil
import os

class Mining():
	""" Kelas untuk melakukan Mining """
	
	DEFAULT_CHAIN_PATH = os.path.join("Blockchain", "store", "mined")
	DEFAULT_PATH_TO_MINE = os.path.join("Blockchain", "store", "pending")

	def start(self):
		""" 
			Memulai proses mining 
			1. Mengambil data dari Blockchain/store/pending
			2. Mengambil block terakhir dari blockchain
			3. Membuat Block baru dengan hash dari block sebelumnya
			4. Menghapus semua data di DEFAULT_PATH_TO_MINE
		"""

		# Mengambil data dari pending block
		controller = Controller()
		dataList = controller.list()
		
		if not dataList:
			ERROR = {
				"msg" : "No need for mining, pending store is clean",
				"code" : "MINING_NOT_NEEDED"
			}
			return ERROR

		# Membuat Chain Baru
		chain, valid = Chain().load(self.DEFAULT_CHAIN_PATH)
		print(valid)
		if valid:
			isChainValid = chain.valid()
			if isChainValid:

				# Membuat Block baru dan melakukan mining
				newBlock = chain.addBlock(dataList)

				# Menghapus semua data block pending
				shutil.rmtree(self.DEFAULT_PATH_TO_MINE)
				os.mkdir(self.DEFAULT_PATH_TO_MINE)
				return newBlock.__dict__
			ERROR = {
				"msg" : "Chain Error! Blockchain can't be generated",
				"code" : "CHAIN_ERROR"
            }
			return ERROR
		return chain