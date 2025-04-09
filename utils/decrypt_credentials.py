from cryptography.fernet import Fernet

def decrypt_credentials():
    with open("config/secret.key", "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    with open("config/credentials.enc", "rb") as file:
        lines = file.readlines()
        username = fernet.decrypt(lines[0].strip()).decode()
        password = fernet.decrypt(lines[1].strip()).decode()

    print(f"🔓 Decrypted username: {username}")
    print(f"🔓 Decrypted password: {password}")
    return username, password
