from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os 
import base64



if os.path.exists("secret.key"):
    with open("secret.key", "rb") as f:
        key = f.read()
else:
    key = AESGCM.generate_key(bit_length=256)
    with open("secret.key", "wb") as f:
        f.write(key)

aesgcm = AESGCM(key)


def encrypt(text):
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, text.encode(), None)
    return base64.b64encode(nonce + ciphertext).decode()


def decrypt(token):
    data = base64.b64decode(token)
    nonce = data[:12]
    ciphertext = data[12:]
    return aesgcm.decrypt(nonce, ciphertext, None).decode()