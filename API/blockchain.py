import hashlib
import json
from datetime import date

# Universal Function
def today_datetime():
    YYYY, MM, DD = date.today().isocalendar()
    return str(DD) + "-" + str(MM) + "-" + str(YYYY)

def timestamp():
    return "tes"

# Block Class
class Block():

  timestamp = ""
  data      = {}
  hash      = ""
  prevHash  = ""
  index     = 0
  nonce     = 0

  def __init__(self, index, timestamp, data, prevHash=""):
      self.timestamp = timestamp
      self.data      = data
      self.prevHash  = prevHash
      self.hash      = self.calculate_hash()
      self.index     = index

  def calculate_hash(self):
      hash = str(self.timestamp) + str(self.data) + str(self.nonce) + str(self.prevHash)
      hash = hash.encode('utf-8')
      return hashlib.sha256(hash).hexdigest()

  def mine_block(self):
      while(self.hash[0] != "b"):
        self.nonce = self.nonce + 1
        self.hash = self.calculate_hash()
        print("{},{},{}".format(self.hash[0], self.hash, self.nonce))

# Blockchain Class
class Blockchain():

  chain = []
  pending_blocks = []

  def __init__(self):
      self.chain = [self.createGenesisBlock()]

  def chainValid(self):
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
      return Block(0,"1-1-2021", "genesis block", "0")

  def getLatestBlock(self):
      return self.chain[len(self.chain) - 1]

  def addBlock(self, block):
      block.prevHash = self.getLatestBlock().hash
      block.mine_block()
      self.chain.append(block)

data = {
  "pasien_id"      : "PS340511902",
  "pasien_nama"    : "Chrisdityra Lengkey",
  "pasien_keluhan" : "Sakit kepala",
  "date_time"      : today_datetime()
}

# Made new blockchain
medicalChain = Blockchain()

# Add new block to blockchain
medicalChain.addBlock(Block(1, today_datetime(), data))
print(medicalChain.chain)

# Check if block is valid
print("Chain Valid : {}".format(medicalChain.chainValid()))
medicalChain.chain[1].data["pasien_id"] = "coba"
print("Chain Valid : {}".format(medicalChain.chainValid()))

medicalChain.addBlock(Block(2, today_datetime(), {"pasien_id": "hello"}))

print(json.dumps(medicalChain.chain[1].__dict__))
print(json.dumps(medicalChain.chain[2].__dict__))
