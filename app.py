import tkinter as tk
import rsaFunctions 

key = None
phi = None
n = None
encryption = None
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
root = tk.Tk()
root.title("RSA Use Case - Mail")

# Set the window size
root.geometry("800x600")  # Width x Height

# Styling
root.configure(bg="#f0f0f0")  # Background color

frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
frame.pack(fill="both", expand=True)

# Create and place widgets with improved styling
message_label = tk.Label(frame, text="Enter message:", font=("Helvetica", 12), bg="#ffffff")
message_label.pack()

message_entry = tk.Entry(frame, font=("Helvetica", 12))
message_entry.pack()

encrypt_button = tk.Button(frame, text="Send Encrypted Message", command=encrypt_message, font=("Helvetica", 12), bg="red")
encrypt_button.pack(pady=10)

public_key_label = tk.Label(frame, text="Public Key Used to Encrypt: ", font=("Helvetica", 12), bg="#ffffff")
public_key_label.pack()

encrypted_label = tk.Label(frame, text="Encrypted Message: ", font=("Helvetica", 12), bg="#ffffff")
encrypted_label.pack()

# Decryption section
decrypt_frame = tk.Frame(frame, bg="#ffffff", padx=10, pady=10)
decrypt_button = tk.Button(decrypt_frame, text="Decrypt", command=decrypt_message, font=("Helvetica", 12), bg="lightblue", fg="#ffffff", state="disabled")
decrypt_button.pack()
decrypt_frame.pack()

decrypted_label = tk.Label(decrypt_frame, text="Decrypted Once received: ", font=("Helvetica", 12), bg="#ffffff")
decrypted_label.pack()

# Start the Tkinter main loop
root.mainloop()
