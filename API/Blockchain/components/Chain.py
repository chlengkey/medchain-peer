from .Block import Block
import os

class Chain():
  """Kelas Blockchain"""

  chain = []
  pending_blocks = []

  def __init__(self, filepath=False):
      """Constructor"""
      self.chain = []
      if filepath:
        self.load(filepath)

  def valid(self):
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
      return Block(0, "Genesis Block", "0")

  def getLatestBlock(self):
      """Mengambil block terakhir dari blockchain"""
      return self.chain[len(self.chain) - 1]

  def addBlock(self, data):
      """Menambahkan block baru ke dalam blockchain"""
      lastBlock = self.getLatestBlock()
      blockIndex = lastBlock.index + 1
      block = Block(blockIndex, data, lastBlock.hash)
      block.mine_block()
      return block

  def load(self, filepath=""):
      blocks = sorted(os.listdir(filepath))
      for block in blocks:
        with open(os.path.join(filepath, block), 'r') as infile:
          loaded_json = infile.read()
          loaded_block = Block(blockData=loaded_json)
          blockFilenameHash = block.split(".")[1]
          if loaded_block.hash != blockFilenameHash:
            ERROR = {
              "msg" : "Error! Invalid block detected",
              "code" : "ILLEGAL_BLOCK_DETECTED"
            }
            return ERROR, False
          self.chain.append(loaded_block)
      return self, True