from rsaFunctions import generatePublicKey, generatePrivateKey, generatePAndQ, calculateN, calculatePhi, returnE, encrypt, decrypt

class Person:
    def __init__(self):
        self.p, self.q = generatePAndQ()
        self.n = calculateN(self.p, self.q)
        self.phi = calculatePhi(self.p, self.q)
        self.e = returnE(self.phi)
        self.public_key = None
        self.private_key = None
        self.message = "HELLO THIS IS THE MESSAGE"
        self.encrypted = ""

    def generate_public_key(self):
        self.public_key = generatePublicKey(self.phi, self.n)
        return self.public_key
    
    def generate_private_key(self):
        self.private_key = generatePrivateKey(self.e, self.phi, self.n)
        return self.private_key

alice = Person()
alice.public_key = alice.generate_public_key()
alice.private_key = alice.generate_private_key()
print(alice.public_key)
print(alice.private_key)
encrypted = encrypt(alice.message, alice.public_key)
alice.encrypted = encrypted
decrypted = decrypt(alice.encrypted, alice.private_key)
print(alice.encrypted)
print(decrypted)