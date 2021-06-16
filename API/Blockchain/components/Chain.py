class Chain():
  """Kelas Blockchain"""

  chain = []
  pending_blocks = []

  def __init__(self):
      """Constructor"""
      self.chain = [self.createGenesisBlock()]

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

  def addBlock(self, block):
      """Menambahkan block baru ke dalam blockchain"""
      block.prevHash = self.getLatestBlock().hash
      block.mine_block()
      self.chain.append(block)