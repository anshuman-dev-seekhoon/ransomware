import os
from cryptography.fernet import Fernet # from encryption one library we imported fernet, basically fernet is a symmetric encryption method which makes sure that the message encrypted cannot be manipulated or read without the key.It uses URL safe encoding for the keys.Fernet also uses 128-bit AES

files = []
for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)   #because it can add directories as well so we want to prevent adding any directory as we want to only encrypt our files


with open("thekey.key","rb") as key:
	secretkey = key.read()

secret_phase = "kiet123"

print("Enter the secret password to access the files: ")
yourcode = str(input())

if yourcode == secret_phase:
	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)   
	print("your files are back: ",files)

	print("Your welcome")
else:
	print("Na maane :) ")
