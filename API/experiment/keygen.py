import sys, os, ast, base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def toBase64(string):
    return base64.b64encode(string)

def generateKeys():
    modulus_length = 4400
    private_key = RSA.generate(modulus_length, Random.new().read)
    public_key  = private_key.public_key()
    return private_key, public_key

if len(sys.argv) == 2:

	# Make the new folder
	if not os.path.isdir(str(sys.argv[1])):
		os.mkdir(str(sys.argv[1]))

	# Export the key
	priv, public = generateKeys()
	privateKey = priv.exportKey()
	publicKey  = public.exportKey()
	print(type(publicKey))
	
	# Menyimpan private key ke dalam file
	file_out = open(sys.argv[1] + "/private.pem", "wb")
	file_out.write(privateKey)
	file_out.close()

	# Menyimpan public key ke dalam file
	file_out = open(sys.argv[1] + "/public.pem", "wb")
	file_out.write(publicKey)
	file_out.close()