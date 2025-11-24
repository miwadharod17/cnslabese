def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


msg = "HELLO World"
shift = 3

enc = caesar_encrypt(msg, shift)
dec = caesar_decrypt(enc, shift)

print("Encrypted:", enc)   # KHOOR Zruog
print("Decrypted:", dec)   # HELLO World

