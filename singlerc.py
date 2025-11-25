def encrypt(text, key):
    text = text.replace(" ", "").lower()
    key_nums = [int(k) for k in key]       # e.g., "4231" → [4,2,3,1]
    cols = len(key_nums)

    # Pad text
    while len(text) % cols != 0:
        text += "x"

    # Make matrix row-wise
    matrix = []
    i = 0
    for _ in range(len(text)//cols):
        matrix.append(list(text[i:i+cols]))
        i += cols
    print(matrix)
    # Read columns according to key order
    cipher = ""
    for n in range(1, cols+1):             # 1,2,3,4
        col = key_nums.index(n)            # find where this number is
        for r in matrix:
            cipher += r[col]

    return cipher

def decrypt(cipher, key):
    key_nums = [int(k) for k in key]
    cols = len(key_nums)
    rows = len(cipher) // cols

    # Empty matrix
    matrix = [[""]*cols for _ in range(rows)]

    # Fill columns in key order
    idx = 0
    for n in range(1, cols+1):         # fill col 1 then 2 then 3...
        col = key_nums.index(n)
        for r in range(rows):
            matrix[r][col] = cipher[idx]
            idx += 1

    # Read row-wise
    plain = ""
    for r in matrix:
        plain += "".join(r)

    return plain

print(encrypt("attackonthem", "4231"))
print(decrypt("anmtkhtoeact", "4231"))
