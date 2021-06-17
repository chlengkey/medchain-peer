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

class Block():
  """kelas untuk block"""

  timestamp = ""
  data      = {}
  hash      = ""
  prevHash  = ""
  index     = 0
  nonce     = 0

  def __init__(self, index=False, data=False, prevHash=False, blockData=False):
      """Constructor untuk kelas block"""

      self.timestamp = timestamp()
      self.data      = data
      self.prevHash  = prevHash
      self.hash      = self.calculate_hash()
      self.index     = index

      if blockData :
        self.load(blockData)


  def calculate_hash(self):
      """Fungsi untuk menghitung hash"""
      hash = str(self.timestamp) + str(self.data) + str(self.nonce) + str(self.prevHash)
      hash = hash.encode('utf-8')
      return hashlib.sha256(hash).hexdigest()

  def mine_block(self, difficulty=4):
      """Fungsi untuk melakukan Mining"""
      while(self.hash[0:difficulty] != str("0").zfill(difficulty)):
        self.nonce = self.nonce + 1
        self.hash = self.calculate_hash()
        print("{},{},{}".format(self.hash[0:2], self.hash, self.nonce))

      # Menambahkan Block Baru
      filepath = "Blockchain/store/mined"
      filename = "{}.{}.json".format(self.index, self.hash)
      finalpath = filepath + "/" + filename
      with open(finalpath, 'w') as outfile:
        json.dump(self.get(), outfile)
        outfile.close()

  def load(self, blockData):
      blockData = json.loads(blockData)
      self.__dict__ = blockData

  def get(self):
      return self.__dict__
      
  def toJson(self):
      return json.dumps(self.__dict__)
