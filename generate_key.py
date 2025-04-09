from utils.encryption import generate_key

key = generate_key()

with open("config/secret.key", "wb") as key_file:
    key_file.write(key)

print("Key generated and saved to config/secret.key:", key)
