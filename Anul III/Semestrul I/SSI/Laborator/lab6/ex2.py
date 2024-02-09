from Crypto.Cipher import AES

key = b'O cheie oarecare'
data = b'testtesttesttesttesttesttesttesttesttesttesttest'

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(data)

print(ciphertext)
