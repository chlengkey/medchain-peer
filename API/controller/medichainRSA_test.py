from medichainRSA import medichainRSA
import sys

data = """{}""".format("tes")

# Load Key
f = open("../local/internal/private.pem")
privateKey = f.read();
privateKey = """{}""".format(privateKey)

f = open("../local/internal/public.pem")
publicKey  = f.read();
publicKey = """{}""".format(publicKey)

if len(sys.argv) == 2:

	# Make instance
	RSAInstance = medichainRSA(privateKey, publicKey)

	# Encrypt a message
	f = open("../local/token/"+sys.argv[1]+"/credential.txt", "r")
	Encrypt = f.read()
	print("Asli : ", Encrypt)
	Decrypt = RSAInstance.decrypt(Encrypt)
	print("\nDekripsi : ", Decrypt)
