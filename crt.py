# ---------- Extended Euclid ----------
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# ---------- Modular Inverse ----------
def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("Inverse does not exist")
    return x % m

# ---------- CRT Combine ----------
# equations: x ≡ r1 (mod n1), x ≡ r2 (mod n2)
def crt(r1, n1, r2, n2):
    # Compute using formula:
    # x = r1 + ( (r2 - r1) * inv(n1, n2) mod n2 ) * n1
    inv = modinv(n1, n2)
    x = (r1 + ((r2 - r1) * inv % n2) * n1) % (n1 * n2)
    return x

# ---------- Example numbers ----------
# Suppose we work mod m1,n1 and m2,n2
r1, n1 = 2, 3
r2, n2 = 3, 5

# ---------- Basic Operations ----------
def crt_add(a1, a2, mod1, b1, b2, mod2):
    return crt((a1 + a2) % mod1, mod1, (b1 + b2) % mod2, mod2)

def crt_sub(a1, a2, mod1, b1, b2, mod2):
    return crt((a1 - a2) % mod1, mod1, (b1 - b2) % mod2, mod2)

def crt_mul(a1, a2, mod1, b1, b2, mod2):
    return crt((a1 * a2) % mod1, mod1, (b1 * b2) % mod2, mod2)

def crt_div(a1, a2, mod1, b1, b2, mod2):
    inv1 = modinv(a2, mod1)
    inv2 = modinv(b2, mod2)
    return crt((a1 * inv1) % mod1, mod1, (b1 * inv2) % mod2, mod2)

# ---------- Testing ----------
print("Add =", crt_add(2, 1, 3, 3, 4, 5))
print("Sub =", crt_sub(2, 1, 3, 3, 4, 5))
print("Mul =", crt_mul(2, 1, 3, 3, 4, 5))
print("Div =", crt_div(2, 1, 3, 3, 4, 5))
