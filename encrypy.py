from cryptography.fernet import Fernet
def load_key():
    return open("secret.key", "rb").read()
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    output_file = filename.replace(".enc", "_decrypted.txt")

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")


choice = input("Choose an option:\n1. Encrypt File\n2. Decrypt File\nEnter choice: ")

file_name = input("Enter file name: ")

if choice == "1":
    encrypt_file(file_name)
elif choice == "2":
    decrypt_file(file_name)
else:
    print("Invalid choice")