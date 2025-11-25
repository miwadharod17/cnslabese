
# Convert letter to number (a=0, b=1, ...)
def char_to_num(ch):
    return ord(ch) - ord('a')

# Convert number to letter
def num_to_char(n):
    return chr(n + ord('a'))

# Prepare text: lowercase, only letters, pad x if odd
def prepare_text(text):
    #text = ''.join(ch.lower() for ch in text if ch.isalpha())
    if len(text) % 2 != 0:
        text += 'x'
    return text

# Multiply 2x2 matrix with 2x1 vector mod 26
def matmul_mod(matrix, vector):
    a, b = matrix[0]
    c, d = matrix[1]
    x, y = vector
    return [
        (a*x + b*y) % 26,
        (c*x + d*y) % 26
    ]

# Find multiplicative inverse mod 26
def mod_inverse(a, m=26):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # No inverse exists

# Hill Encryption
def hill_encrypt(text, key):
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        x = char_to_num(text[i])
        y = char_to_num(text[i+1])

        r = matmul_mod(key, [x, y])

        cipher += num_to_char(r[0])
        cipher += num_to_char(r[1])

    return cipher

# Hill Decryption
def hill_decrypt(cipher, key):
    # determinant
    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26

    det_inv = mod_inverse(det)
    if det_inv is None:
        raise ValueError("Key matrix is not invertible modulo 26!")

    # adjoint
    adj = [
        [ key[1][1], -key[0][1]],
        [-key[1][0],  key[0][0]]
    ]

    # inverse matrix mod 26
    inv_key = [
        [(det_inv * adj[0][0]) % 26, (det_inv * adj[0][1]) % 26],
        [(det_inv * adj[1][0]) % 26, (det_inv * adj[1][1]) % 26]
    ]

    plain = ""

    for i in range(0, len(cipher), 2):
        x = char_to_num(cipher[i])
        y = char_to_num(cipher[i+1])

        r = matmul_mod(inv_key, [x, y])

        plain += num_to_char(r[0])
        plain += num_to_char(r[1])

    return plain


# -------------------------
# Example Use
# -------------------------
key = [
    [3, 3],
    [2, 5]
]

plaintext = "help"

encrypted = hill_encrypt(plaintext, key)
decrypted = hill_decrypt(encrypted, key)

print("Plaintext :", plaintext)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
