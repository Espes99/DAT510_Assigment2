from rsaFunctions import generatePublicKey, generatePrivateKey, generatePAndQ, calculateN, calculatePhi, returnE, encrypt, decrypt

class Person:
    def __init__(self):
        self.p, self.q = generatePAndQ()
        self.n = calculateN(self.p, self.q)
        self.phi = calculatePhi(self.p, self.q)
        self.e = returnE(self.phi)
        self.public_key = None
        self.private_key = None
        self.message = ""
        self.encrypted = ""

    def generate_public_key(self):
        self.public_key = generatePublicKey(self.phi, self.n)
        return self.public_key
    
    def generate_private_key(self):
        self.private_key = generatePrivateKey(self.e, self.phi, self.n)
        return self.private_key

alice = Person()
bob = Person()
alice.public_key = alice.generate_public_key()
alice.private_key = alice.generate_private_key()
bob.public_key = bob.generate_public_key()
bob.private_key = bob.generate_private_key()
if alice.public_key is None:
    print("alice.public_key is None")
else:
    alice.private_key = alice.generate_private_key()
    print("A pub", alice.private_key)

if alice.private_key is None:
    print("alice.private_key is None")
else:
    alice.private_key = alice.generate_private_key()
    print("A priv", alice.private_key)

if bob.public_key is None:
    print("bob.public_key is None")
else:
    print("B pub", bob.public_key)
if bob.private_key is None:
    print("bob.private_key is None")
else:
    print("B priv", bob.private_key)

bob.messsage = "Hello, this is bob"
alice.encrypted = encrypt(bob.message, alice.public_key)
print(alice.encrypted)
#Alice receives the encrypted message from Bob
bob.message = decrypt(alice.encrypted, alice.private_key)
print(bob.message)
