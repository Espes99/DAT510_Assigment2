import random
#Get all letters from A to Z and map them to numbers from 0 to 25, an additional parameter is added for space
letterToNumber = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 
                      'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 
                      'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26, ',': 27, '.': 28, '!': 29, '?': 30}


# Function to reverse the mapping and return the letter for a given numeric value
def numberToLetter(num):
        for letter, value in letterToNumber.items():
            if value == num:
                return letter

#Very basic function of determining if a number is prime
#Iterate through all numbers from 2 to n-1 and check if n is divisible by any of them without a remainder
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


#Randomize p until it is prime
#Find p and q Small prime numbers for demonstration, but you would want to create large numbers for real use, like numbers greater than 1024 bits
def generatePrimeNumber(min=1000, max=2000):
    p = random.randint(min, max)
    while not isPrime(p):
        p = random.randint(min, max)
    return p


#Generate large prime numbers using getrandbits() function
#This method is not efficient do to my function of determining prime numbers
#I determine prime numbers by looping through all numbers from 2 to n-1 and checking if n is divisible by any of them
#When the number is of 1024 bits, it takes a great amount of time to generate prime numbers
def generateLargeNumberByBits(bits=1024):
    candidate = random.getrandbits(bits)
    while not isPrime(candidate):
        candidate = random.getrandbits(bits)
    return candidate

#Generate p and q, where p and q are prime numbers and p != q
def generatePAndQ():
    p = generatePrimeNumber()
    q = generatePrimeNumber()
    while p == q:
        q = generatePrimeNumber()
    return p, q

#Calculate n, where n = p * q
def calculateN(p, q):
    n = p * q
    return n

#Calculate phi, where phi = (p-1)*(q-1), phi is essentially all numbers coprime with n, and less than n
def calculatePhi(p,q):
    phi = (p-1)*(q-1)
    return phi

#Finding gcd using euclidean algorithm 
#Loop through until b is 0
def gcd(a, b):
    while b:
        remainder = a % b
        a = b
        b = remainder
    #When b is 0, a will be the greatest common divisor of a and b    
    return a

# Pick an e, where e is greater than 2 and less than phi(n) and coprime to phi(n) and n -> e is public key, phi > e > 2 && gcd(e,phi(n)) = 1 
def returnE(phi):
    e = random.randint(3, phi-1) #Fullfils requirement of phi > e > 2, randint includes both endpoint, hence phi-1
    while gcd(e, phi) != 1: #As long as they are not coprime, generate e
        e = random.randint(3, phi-1)
    return e

#Find a multiplicative inverse in modular phi, is a number d such that e*d ≡ 1 mod phi
def modularInverse(e, phi):
    d = pow(e, -1, phi)
    return d

#Function to return public key
def generatePublicKey(phi, n):
    e = returnE(phi)
    return e,n

#Function to return public key
def generatePrivateKey(e, phi, n):
    d = modularInverse(e, phi)
    return d,n

# Now, you have the public key (e,n) and private key (d,n)

# Function to encrypt a message by encrypting using the public key and the numeric value of each character
#Used pow(), takes in x (basevalue) and y (exponent) and z(modulus) and returns x^y modulus z
#pow(char, e, n) - (char^r) mod n
def encrypt(plainText, publicKey):
    e = publicKey[0]
    n = publicKey[1]
    plainText = plainText.upper()
    cipherText = []
    for char in plainText:
        numericValue = letterToNumber[char]
        encryptedCharValue = pow(numericValue, e, n)
        cipherText.append(encryptedCharValue)
    return cipherText # This maps same char to same values. Should do block-wise


# Function to decrypt a message by decrypting using the private key and the numeric value of each character
#Used pow(), takes in x (basevalue) and y (exponent) and z(modulus) and returns x^y modulus z
#pow(char, e, n) - (char^r) mod n
def decrypt(cipherText, privateKey):
    d = privateKey[0]
    n = privateKey[1]
    plainText = ""
    for encryptedChar in cipherText:
        numericValue = pow(encryptedChar, d, n)
        char = numberToLetter(numericValue)
        if char is None:
            plainText += " "
        else:
            plainText += char
    return plainText
