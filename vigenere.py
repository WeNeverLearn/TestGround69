import string

LETTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + " "
L = len(LETTERS)

def encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise Exception("PLAINTEXT_AND_KEY_NOT_EQUAL_IN_LENGTH")

    c = ""

    for i, j in zip(plaintext, key):
        m = LETTERS.index(i)
        k = LETTERS.index(j)
        char_index = (m + k) % L
        c += LETTERS[char_index]

    return c

def decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise Exception("CIPHER_AND_KEY_NOT_EQUAL_IN_LENGTH")

    m = ""

    for i, j in zip(ciphertext, key):
        c = LETTERS.index(i)
        k = LETTERS.index(j)
        char_index = (c - k) % L
        m += LETTERS[char_index]

    return m
