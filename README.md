# Assignment 2 - RSA

## Introduction

This repository contains Python files for implementing the RSA encryption and decryption algorithm. RSA is a widely-used asymmetric key encryption algorithm that allows for secure communication over insecure channels.

## Files Included

1. **app.py**

   - Description: This file contains a graphical user interface (GUI) for encrypting and decrypting messages using the RSA algorithm. It uses the `rsaFunctions` module to perform encryption and decryption operations.

2. **rsaFunctions.py**

   - Description: This module contains the core functions required for RSA encryption and decryption. It includes functions for generating prime numbers, calculating `n` and `phi`, generating public and private keys, and encrypting/decrypting messages.

3. **Person.py**

   - Description: This file demonstrates the generation of RSA key pairs for a person, encryption of a message using the person's public key, and decryption using their private key.

## Usage Instructions

### app.py

1. Run `app.py` using Python to open the RSA Use Case - Mail GUI.

2. Enter your message in the "Enter message" field.

3. Click the "Send Encrypted Message" button to encrypt the message. The public key used for encryption and the encrypted message will be displayed.

4. To decrypt the message, click the "Decrypt" button. The decrypted message will be displayed in the GUI.

### Person.py

1. Run `Person.py` using Python.

2. The script will create an instance of a person (Alice) and generate her RSA key pair. It will then encrypt a message and decrypt it to demonstrate the process.

3. The public key, private key, and the original, encrypted, and decrypted messages will be printed to the console.

## Key Concepts

- **RSA Encryption:** The RSA algorithm is used to encrypt the message, ensuring secure communication.

- **Key Pair Generation:** RSA key pairs, including public and private keys, are generated using the `rsaFunctions` module.

- **Message Encryption:** The message is encrypted using the public key.

- **Message Decryption:** The recipient can decrypt the message using the private key.

- **Digital Signature (mentioned in comments):** RSA can also be used for digital signatures. This is briefly mentioned in the comments, where Alice signs a message for Bob, and Bob can verify the signature using Alice's public key.
- Bob sends a document to Alice - M = 20. Ciphertext = M^e mod n (e, n) public key. For example Ciphertext = 340.
- Alice will use her private key Message = 340^d mod n. Message = 20. 
- Alice generates a Signature to sign document - M^d mod n (d private), for example S = 200. Bob recipient takes 200^e mod n = 20. 
