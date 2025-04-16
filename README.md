🔐 Linux Ransomware Simulation – encrypt.py & decrypt.py
⚠️ Disclaimer

This project is for educational and ethical testing purposes only. It is designed to demonstrate how ransomware operates in a controlled environment. Unauthorized use of this code on systems without explicit permission is illegal and unethical.​
Medium
📁 Project Overview

This project simulates a basic ransomware attack on Linux systems using Python. It comprises two scripts:

    encrypt.py: Encrypts files within a specified directory using symmetric encryption.​
    DEV Community+2CodeSandbox+2GitHub+2

    decrypt.py: Decrypts the previously encrypted files using the correct key.​

🧠 How It Works
encrypt.py:

    Key Generation: Generates a symmetric encryption key using the cryptography library.​
    Easyread

    File Discovery: Recursively searches for files in the specified directory to encrypt.​

    Encryption: Encrypts each file and saves the key to a file named thekey.key.​
    GitHub+1DEV Community+1

    Ransom Note: Optionally, creates a ransom note informing the user of the encryption.​

decrypt.py:

    Key Retrieval: Reads the encryption key from thekey.key.​

    File Discovery: Recursively searches for encrypted files in the specified directory.​

    Decryption: Decrypts each file using the retrieved key.​
    GitHub+1Cyber Security and Programming+1

🛠️ Setup & Usage
Prerequisites

    Python 3.x​

    cryptography library​
    thepythoncode.com+2Easyread+2Cyber Security and Programming+2

    pip install cryptography

Usage

    Encryption:

python3 encrypt.py /path/to/target/directory

Decryption:

    python3 decrypt.py /path/to/target/directory

🧪 Example

# Encrypt files in the 'Documents' directory
python3 encrypt.py ~/Documents

# Decrypt files in the 'Documents' directory
python3 decrypt.py ~/Documents
🧠 Learning Objectives

    Understand the basics of symmetric encryption using Python.​

    Learn how ransomware encrypts and decrypts files.​

    Recognize the importance of cybersecurity and ethical hacking practices.​
    GitHub

📌 Important Notes

    Always run this code in a controlled environment, such as a virtual machine.​

    Ensure you have backups of any data before testing.​

    Do not deploy or distribute this code for malicious purposes.​

📚 References

    Cryptography Library Documentation​
    Cyber Security and Programming+2thepythoncode.com+2Easyread+2

    Python Official Documentation
