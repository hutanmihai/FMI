from Crypto.Cipher import DES

# key1 = b'\x?0\x00\x00\x00\x00\x00\x00\x00'
# key2 = b'\x?0\x00\x00\x00\x00\x00\x00\x00'
#
# cipher1 = DES.new(key1, DES.MODE_ECB)
# cipher2 = DES.new(key2, DES.MODE_ECB)

PLAINTEXT = b'Provocare MitM!!'
# ciphertext = cipher2.encrypt(cipher1.encrypt(plain_text_val))

# Solution starts here
SUFFIX = b'\x00\x00\x00\x00\x00\x00\x00'
CIPHERTEXT = b"G\xfd\xdfpd\xa5\xc9'C\xe2\xf0\x84)\xef\xeb\xf9"


def encrypt_text(val, plaintext=PLAINTEXT):
    val = val * 16
    key = bytes([val]) + SUFFIX  # Transform the value in bytes and concatenate it with the suffix
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plaintext)


def decrypt_text(val, ciphertext=CIPHERTEXT):
    val = val * 16
    key = bytes([val]) + SUFFIX  # Transform the value in bytes and concatenate it with the suffix
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(ciphertext)


def mitm():
    dictionary = {}
    candidates = []

    # Encrypt the plaintext with all the possible keys and store the result in a dictionary
    for key in range(16):
        code = str(encrypt_text(key))
        if code not in dictionary:
            dictionary[code] = key

    for key2 in range(16):
        intermediate_result = str(decrypt_text(key2))

        if intermediate_result in dictionary:
            candidate = (key2, dictionary[intermediate_result])

            if decrypt_text(candidate[1], decrypt_text(candidate[0])) == PLAINTEXT:
                candidates.append(candidate)

    if len(candidates) == 0:
        return None
    return candidates


if __name__ == '__main__':
    response = mitm()

    if response is None:
        exit("Not found!")

    for key in response:
        print("Cheile sunt: ")
        key1_int = key[0]
        key2_int = key[1]
        key1 = key[0] * 16
        key2 = key[1] * 16
        print(bytes([key1]) + SUFFIX)
        print(bytes([key2]) + SUFFIX)

        print("Deci semnele intrebarii sunt inlocuite de cifrele hexa:")
        print(key1_int, key2_int)

    # MiTM cripteaza si decripteaza cate 2^k+1 key. In total au fost testate 32 de chei.
