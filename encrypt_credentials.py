from utils.encryption import load_key, encrypt_data
import os

# Load the encryption key
key = load_key()

# Input credentials (or use test/demo ones)
username = input("Enter username: ")
password = input("Enter password: ")

# Encrypt credentials
enc_username = encrypt_data(username, key)
enc_password = encrypt_data(password, key)

# Save to file
os.makedirs("config", exist_ok=True)
with open("config/credentials.enc", "wb") as file:
    file.write(enc_username + b"\n" + enc_password)

print("Encrypted credentials saved to config/credentials.enc")
