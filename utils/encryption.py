from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("config/secret.key", "wb") as key_file:
        key_file.write(key)
    print(f"Key generated and saved to config/secret.key: {key}")
    return key

def load_key():
    with open("config/secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

