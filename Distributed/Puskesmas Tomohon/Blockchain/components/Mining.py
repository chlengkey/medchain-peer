from .Block import Block
from .Chain import Chain
from Data.components.Controller import Controller
import shutil
import os

class Mining():
	""" Kelas untuk melakukan Mining """
	
	DEFAULT_CHAIN_PATH = os.path.join("Blockchain", "store", "mined")
	DEFAULT_PATH_TO_MINE = os.path.join("Blockchain", "store", "pending")

	def get_pending_data(self):

		# Mengambil data dari pending block
		controller = Controller()
		dataList = controller.list()

		if not dataList:
			ERROR = {
				"msg" : "Mining belum dibutuhkan untuk saat ini",
				"code" : "MINING_NOT_NEEDED"
			}
			return False, ERROR
		print(dataList)
		print("Check")
		return True, dataList

	def start(self):
		""" 
			Memulai proses mining 
			1. Mengambil data dari Blockchain/store/pending
			2. Mengambil block terakhir dari blockchain
			3. Membuat Block baru dengan hash dari block sebelumnya
			4. Menghapus semua data di DEFAULT_PATH_TO_MINE
		"""
		pending_data_exists, dataList = self.get_pending_data()
		if not pending_data_exists:
			return dataList

		# Membuat Chain Baru
		chain, valid = Chain().load(self.DEFAULT_CHAIN_PATH)

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