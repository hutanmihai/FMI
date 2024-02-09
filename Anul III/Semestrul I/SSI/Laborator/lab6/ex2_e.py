from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'O cheie oarecare'
data = b'test'

# Adaugăm padding la data pentru a fi multiplu de 16
data = pad(data, AES.block_size)

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(data)

print(ciphertext)
