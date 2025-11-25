def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def caesar_encrypt(text, shift):
    base=ord('a')
    result=""
    for ch in text:
        if ch.isalpha():
            result+=chr((ord(ch)-base+shift)%26 + base)
        else:
            result+=ch
    return result

msg = "hello world"
shift = 3

enc = caesar_encrypt(msg, shift)
dec = caesar_decrypt(enc, shift)

print("Encrypted:", enc)   # KHOOR Zruog
print("Decrypted:", dec)   # HELLO World

