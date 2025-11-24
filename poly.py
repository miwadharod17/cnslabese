def vigenere_encrypt(text, key):
    text = text.lower()
    key = key.lower()
    cipher = ""

    k = 0  # index for key

    for ch in text:
        if ch.isalpha():
            shift = ord(key[k % len(key)]) - ord('a')
            cipher += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            k += 1
        else:
            cipher += ch  # preserve spaces/punctuation

    return cipher


def vigenere_decrypt(cipher, key):
    cipher = cipher.lower()
    key = key.lower()
    text = ""

    k = 0

    for ch in cipher:
        if ch.isalpha():
            shift = ord(key[k % len(key)]) - ord('a')
            text += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            k += 1
        else:
            text += ch

    return text

plaintext = "attack at dawn"
key = "lemon"

enc = vigenere_encrypt(plaintext, key)
dec = vigenere_decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
