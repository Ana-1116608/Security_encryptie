from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os 

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

nonce = os.urandom(12)
tekst = "hallo wereld"
geheim = aesgcm.encrypt(nonce, tekst.encode(), None)
print(geheim)
terug = aesgcm.decrypt(nonce, geheim, None)
print(terug.decode())