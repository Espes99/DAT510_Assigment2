# Assignment 2 - RSA

## Overview

This project includes basic implementation of RSA encryption and decryption with a very basic GUI. It was meant to be a simulated sending service by mail. With a sender and a receiver. 
Ideally, the keypair generation should use high values of p and q. But due to demonstration purposes only, these numbers have been reduced to a be chosen from 1000-2000. The function: `def generateLargeNumberByBits(bits=1024):` can be used to generate large numbers. However, if this is to be used, there will need to be configuration in verifying its prime properties. My implementation is not efficient enough for large numbers.  

## Files

1. **app.py**: This file contains the very basic graphical user interface (GUI) for encrypting and decrypting messages using the RSA algorithm. It uses the `rsaFunctions` module to perform encryption and decryption operations.

2. **rsaFunctions.py**: This module contains the core functions required for RSA encryption and decryption. It includes functions for generating prime numbers, calculating `n` and `phi`, generating public and private keys, and encrypting/decrypting messages.

3. **Person.py**: Provides a class for generation of RSA key pairs for a person, encryption of a message using the person's public key, and decryption using their private key.
### NOTE: The Person class is unused at this moment due to variable issues. I have been unable to resolve this issue. 
## Usage Instructions

### Usage

1. Run `app.py` using Python to open the RSA Use Case - Mail GUI.

2. Enter your message in the "Enter message" field. The decryption button is disabled until there's a message to encrypt

3. Click the "Send Encrypted Message" button to encrypt the message. The public key used for encryption and the encrypted message will be displayed, which is the case also in real world scenarios. 

4. To decrypt the message, click the "Decrypt" button. The decrypted message will be displayed in the GUI. This is to simulate a received message from the sender. 

### Person.py
*As mentioned, this is not working properly*
1. Run `Person.py` using Python.

2. The script will create an instance of a person (Alice) and generate her RSA key pair. It will then encrypt a message and decrypt it to demonstrate the process.

3. The public key, private key, and the original, encrypted, and decrypted messages will be printed to the console.

## Key Concepts

- **RSA Encryption:** The RSA algorithm is used to encrypt the message, ensuring secure communication.

- **Key Pair Generation:** RSA key pairs, including public and private keys, are generated using the `rsaFunctions` module.

- **Message Encryption:** The message is encrypted using the public key.

- **Message Decryption:** The recipient can decrypt the message using the private key.

- **Digital Signature (mentioned in comments):** RSA can also be used for digital signatures. This is briefly mentioned in the comments, where Alice signs a message for Bob, and Bob can verify the signature using Alice's public key.

## Notes

This application is implemented as motivation of an assignment in Security and Vulnerability in Networks at UiS. The application is intended for educational purposes only and should not be used for any other purposes.
