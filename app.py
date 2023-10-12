import tkinter as tk
import rsaFunctions 

#Having global fields for phi is not ideal. The phi is to be kept a secret. 
#I had issues in fetching the phi from the encrypt_message() function
key = None
phi = None
n = None
encryption = None

#Encryption for the GUI
def encrypt_message():
    global key
    global phi
    global n
    global encryption
    message = message_entry.get()
    p, q = rsaFunctions.generatePAndQ()
    n = rsaFunctions.calculateN(p, q)
    phi = rsaFunctions.calculatePhi(p, q)
    key = rsaFunctions.generatePublicKey(phi, n)
    public_key_label.config(text=f"Public Key Used to Encrypt: {key}")
    encryption = rsaFunctions.encrypt(message, key)
    encrypted_label.config(text=f"Encrypted Message: {encryption}")
    
    # Enable the decryption button
    decrypt_button.config(state="normal")

#Decryption method for GUI
def decrypt_message():
    global key  # Use the global key variable
    global encryption
    if key is not None and encryption is not None:
        private_key = rsaFunctions.generatePrivateKey(key[0], phi, n)
        decrypted = rsaFunctions.decrypt(encryption, private_key)
        decrypted_label.config(text=f"Decrypted Once received: {decrypted}")
    else:
        print("Key or encryption was none")

# Create the main window
window = tk.Tk()
window.title("RSA Use Case - Mail")

# Styling
window.configure()  # Background color

frame = tk.Frame(window)
frame.pack(fill="both")

#Creating label - Enter message
message_label = tk.Label(frame, text="Enter message:", font=("Helvetica", 12))
message_label.pack()

#Creating entry field for message
message_entry = tk.Entry(frame, font=("Helvetica", 12))
message_entry.pack()

#Creating button - Send encrypted message
encrypt_button = tk.Button(frame, text="Send Encrypted Message", command=encrypt_message, font=("Helvetica", 12), bg="red")
encrypt_button.pack(pady=10)

#Creating label - Public key used to encrypt
public_key_label = tk.Label(frame, text="Public Key Used to Encrypt: ", font=("Helvetica", 12))
public_key_label.pack()

#Creating label - Encrypted message
encrypted_label = tk.Label(frame, text="Encrypted Message: ", font=("Helvetica", 12))
encrypted_label.pack()

# Decryption section
decrypt_frame = tk.Frame(frame, padx=10, pady=10)

#Decrypt button to get message, orignally disabled until message is encrypted
decrypt_button = tk.Button(decrypt_frame, text="Decrypt", command=decrypt_message, font=("Helvetica", 12), bg="lightblue", state="disabled")
decrypt_button.pack()
decrypt_frame.pack()

#Decrypted message
decrypted_label = tk.Label(decrypt_frame, text="Decrypted Once received: ", font=("Helvetica", 12))
decrypted_label.pack()

window.mainloop()

#What I wanted to achieve by using Person() and then use to people - Alice and Bob
#Bob sends message
#Alice decrypts message
#Alice have her own keypair -
#Public key (e,n) is public
#Bob sends a message to Alice using public Key - C = M^e mod n
#Alice reverses cipher text with private key (d,e), d is multiplicative inverse of e
# M = M^d mod n


#Signing a message
#Alice sends a message to Bob, and generates a signature = M^d mod n
#Bob verifies the signature by using public key (e,n) and checks if M = S^e mod n