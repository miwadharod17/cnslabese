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


def rsa_encrypt(m, e, n):
    return pow(m, e, n)


def rsa_decrypt(c, d, n):
    return pow(c, d, n)


# -------------------------------
# Combined RSA + Caesar
# -------------------------------

def hybrid_encrypt(text, shift, e, n):
    """
    Step 1: Caesar encrypt text
    Step 2: Convert each character to ASCII and RSA encrypt
    """
    caesar_out = caesar_encrypt(text, shift)
    rsa_out = [rsa_encrypt(ord(ch), e, n) for ch in caesar_out]
    return rsa_out


def hybrid_decrypt(cipher_list, shift, d, n):
    """
    Step 1: RSA decrypt each number → ASCII
    Step 2: Run Caesar decrypt
    """
    rsa_decrypted = ''.join(chr(rsa_decrypt(c, d, n)) for c in cipher_list)
    plain = caesar_decrypt(rsa_decrypted, shift)
    return plain


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Example RSA keys
    p = 61
    q = 53
    n = p * q                 # 3233
    phi = (p - 1) * (q - 1)   # 3120
    e = 17
    d = 2753                  # modular inverse of 17 mod 3120

    shift = 3
    message = "HELLO"

    print("Original:", message)

    encrypted = hybrid_encrypt(message, shift, e, n)
    print("Encrypted (RSA of Caesar):", encrypted)

    decrypted = hybrid_decrypt(encrypted, shift, d, n)
    print("Decrypted:", decrypted)
