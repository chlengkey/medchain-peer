import hashlib
import json
from datetime import date
import time

# Universal Function
def today_datetime():
    YYYY, MM, DD = date.today().isocalendar()
    return str(DD) + "-" + str(MM) + "-" + str(YYYY)

def timestamp():
    return time.time()

# Block Class
class Block():
  """kelas untuk block"""

  timestamp = ""
  data      = {}
  hash      = ""
  prevHash  = ""
  index     = 0
  nonce     = 0

  def __init__(self, index, data, prevHash=""):
      """Constructor untuk kelas block"""
      self.timestamp = timestamp()
      self.data      = data
      self.prevHash  = prevHash
      self.hash      = self.calculate_hash()
      self.index     = index

  def calculate_hash(self):
      """Fungsi untuk menghitung hash"""
      hash = str(self.timestamp) + str(self.data) + str(self.nonce) + str(self.prevHash)
      hash = hash.encode('utf-8')
      return hashlib.sha256(hash).hexdigest()

  def mine_block(self, difficulty=4):
      """Fungsi untuk melakukan mining"""
      while(self.hash[0:difficulty] != str("0").zfill(difficulty)):
        self.nonce = self.nonce + 1
        self.hash = self.calculate_hash()
        print("{},{},{}".format(self.hash[0:2], self.hash, self.nonce))

# Blockchain Class
class Blockchain():
  """Kelas Blockchain"""

  chain = []
  pending_blocks = []

  def __init__(self):
      """Constructor"""
      self.chain = [self.createGenesisBlock()]

  def chainValid(self):
      """Apakah blockchain valid?"""
      if(len(self.chain) > 1):
         blockIndex = 1
         while(blockIndex <= (len(self.chain) - 1)):
             currentBlock  = self.chain[blockIndex]
             previousBlock = self.chain[blockIndex - 1]

             if (currentBlock.hash != currentBlock.calculate_hash()):
                print("\nBlock[{}] is not valid".format(currentBlock.index))
                print("Expected Hash : {}".format(currentBlock.calculate_hash()))
                print("Actual Hash   : {}\n".format(currentBlock.hash))
                return False

             if (previousBlock.hash != currentBlock.prevHash):
                print("Previous Hash from block[{}] is not match with block[{}] hash".format(blockIndex - 1, blockIndex))
                return False
             blockIndex = blockIndex + 1
      return True

  def createGenesisBlock(self):
      """Membuat genesis block"""
      return Block(0, "genesis block", "0")

  def getLatestBlock(self):
      """Mengambil block terakhir dari blockchain"""
      return self.chain[len(self.chain) - 1]

  def addBlock(self, block):
      """Menambahkan block baru ke dalam blockchain"""
      block.prevHash = self.getLatestBlock().hash
      block.mine_block()
      self.chain.append(block)