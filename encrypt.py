from cryptography.fernet import Fernet
import os
# key generation
# key = Fernet.generate_key()
#
# # string the key in a file
# with open('filekey.key', 'wb') as filekey:
#     filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
    print(key)

# using the generated key
fernet = Fernet(key)

def encrypt(file):
    # opening the original file to encrypt

    with open(file, 'rb') as f:
        original = f.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(file+".bin", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(file)


def decrypt(file):

    # opening the encrypted file

    with open(file, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open(file.rsplit(".bin")[0], 'wb') as dec_file:
        dec_file.write(decrypted)
        os.remove(file)
