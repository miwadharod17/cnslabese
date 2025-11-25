# ---------- Extended Euclid ----------
def egcd(a, b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2

        s = s1 - q * s2
        t = t1 - q * t2

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    return r1, s1, t1   

# ---------- Modular Inverse ----------
def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("Inverse does not exist")
    return x % m

# ---------- CRT Combine ----------
def crt_general(remainders, moduli):
    """Compute integer from CRT remainders"""
    M = 1
    for m in moduli:
        M *= m

    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        yi = modinv(Mi, m)
        x += r * Mi * yi

    return x % M

def to_crt(number, moduli):
    return [number % m for m in moduli]

# ---------- Example numbers ----------

# ---------- Basic Operations ----------
def crt_add(A, B, moduli):
    C = [(a + b) % m for a, b, m in zip(A, B, moduli)]
    return crt_general(C, moduli)

def crt_sub(A, B, moduli):
    C = [(a - b) % m for a, b, m in zip(A, B, moduli)]
    return crt_general(C, moduli)

def crt_mul(A, B, moduli):
    C = [(a * b) % m for a, b, m in zip(A, B, moduli)]
    return crt_general(C, moduli)

def crt_div(A, B, moduli):
    # Division: multiply by modular inverse of B mod each modulus
    C = [(a * modinv(b, m)) % m for a, b, m in zip(A, B, moduli)]
    return crt_general(C, moduli)


# ---------- Testing ----------
moduli = [3, 5, 7]
A = 11
B = 8

A_crt = to_crt(A, moduli)  # [2, 3, 1]
B_crt = to_crt(B, moduli)  # [1, 2, 0]

print("CRT Add =", crt_add(A_crt, B_crt, moduli))
print("CRT Sub =", crt_sub(A_crt, B_crt, moduli))
print("CRT Mul =", crt_mul(A_crt, B_crt, moduli))
print("CRT Div =", crt_div(A_crt, B_crt, moduli))
