import numpy as np

# Convert letter to number (A=0, B=1, ...)
def char_to_num(ch):
    return ord(ch) - ord('a')

# Convert number back to letter
def num_to_char(n):
    return chr(n + ord('a'))

# Prepare text: lowercase, remove spaces, pad with 'x' if odd length
def prepare_text(text):
    text = ''.join(ch.lower() for ch in text if ch.isalpha())
    if len(text) % 2 != 0:
        text += 'x'
    return text

# Hill encryption
def hill_encrypt(text, key):
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        pair = np.array([[char_to_num(text[i])],
                         [char_to_num(text[i+1])]])

        result = np.dot(key, pair) % 26

        cipher += num_to_char(result[0][0])
        cipher += num_to_char(result[1][0])

    return cipher

# Hill decryption
def hill_decrypt(cipher, key):
    # Find determinant inverse mod 26
    det = int(np.round(np.linalg.det(key)))
    det = det % 26

    # Multiplicative inverse of determinant mod 26
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break

    # Inverse matrix modulo 26
    inv_key = (
        det_inv *
        np.array([[ key[1][1], -key[0][1]],
                  [-key[1][0],  key[0][0]]])
    ) % 26

    plain = ""

    for i in range(0, len(cipher), 2):
        pair = np.array([[char_to_num(cipher[i])],
                         [char_to_num(cipher[i+1])]])

        result = np.dot(inv_key, pair) % 26

        plain += num_to_char(result[0][0])
        plain += num_to_char(result[1][0])

    return plain


# -------------------------
# Example Use
# -------------------------
if __name__ == "__main__":
    key = np.array([[3, 3],
                    [2, 5]])   # Standard invertible matrix mod 26

    plaintext = "help"

    encrypted = hill_encrypt(plaintext, key)
    decrypted = hill_decrypt(encrypted, key)

    print("Plaintext :", plaintext)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)


##############
