from blockchain import Blockchain, Block
import json

medicalChain = Blockchain()
medicalChain.addBlock(Block(1, {"pasien_nama" : "Cleonart"}))
print(json.dumps(medicalChain.chain[1].__dict__))
