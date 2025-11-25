import string

# ------------------------
# 1. Generate 5x5 Playfair Key Square
# ------------------------
def generate_key_square(key):
    key = key.lower().replace("j", "i")
    seen = set()
    key_square = []

    for ch in key + string.ascii_lowercase:
        if ch == 'j':
            continue
        if ch not in seen and ch.isalpha():
            seen.add(ch)
            key_square.append(ch)

        if len(key_square) == 25:
            break

    return [key_square[i:i+5] for i in range(0, 25, 5)]


# ------------------------
# 2. Prepare plaintext
# ------------------------
def prepare_text(text):
    text = text.lower().replace("j", "i")
    text = ''.join(ch for ch in text if ch.isalpha())

    # If odd length → add tail X
    if len(text) % 2 != 0:
        text += 'x'

    # Form digraphs normally (no repeated-letter rule)
    return [text[i:i+2] for i in range(0, len(text), 2)]



# ------------------------
# 3. Find position in key square
# ------------------------
def find_position(square, ch):
    for i in range(5):
        for j in range(5):
            if square[i][j] == ch:
                return i, j
    return None


# ------------------------
# 4. Encrypt digram
# ------------------------
def encrypt_digram(a, b, square):
    r1, c1 = find_position(square, a)
    r2, c2 = find_position(square, b)

    # Rule 1: Same row
    if r1 == r2:
        return square[r1][(c1+1)%5] + square[r2][(c2+1)%5]

    # Rule 2: Same column
    if c1 == c2:
        return square[(r1+1)%5][c1] + square[(r2+1)%5][c2]

    # Rule 3: Rectangle rule
    return square[r1][c2] + square[r2][c1]


# ------------------------
# 5. Decrypt digram
# ------------------------
def decrypt_digram(a, b, square):
    r1, c1 = find_position(square, a)
    r2, c2 = find_position(square, b)

    # Same row: move left
    if r1 == r2:
        return square[r1][(c1-1)%5] + square[r2][(c2-1)%5]

    # Same column: move up
    if c1 == c2:
        return square[(r1-1)%5][c1] + square[(r2-1)%5][c2]

    # Rectangle rule
    return square[r1][c2] + square[r2][c1]


# ------------------------
# 6. Full Encryption
# ------------------------
def playfair_encrypt(text, key):
    square = generate_key_square(key)
    pairs = prepare_text(text)
    cipher = ''.join(encrypt_digram(a, b, square) for a, b in pairs)
    return cipher


# ------------------------
# 7. Full Decryption
# ------------------------
def playfair_decrypt(cipher, key):
    square = generate_key_square(key)
    pairs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]
    plain = ''.join(decrypt_digram(a, b, square) for a, b in pairs)
    return plain


# ------------------------
# Example
# ------------------------
if __name__ == "__main__":
    key = "MONARCHY"
    text = "JUICE"

    encrypted = playfair_encrypt(text, key)
    decrypted = playfair_decrypt(encrypted, key)

    print("Key Square:")
    for row in generate_key_square(key):
        print(row)

    print("\nPlaintext:", text)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
