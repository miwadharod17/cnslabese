def extended_euclid(a, b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    print("r1\t r2\t q\t r\t s1\t s2\t s\t t1\t t2\t t")

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2

        s = s1 - q * s2
        t = t1 - q * t2

        print(f"{r1}\t {r2}\t {q}\t {r}\t {s1}\t {s2}\t {s}\t {t1}\t {t2}\t {t}")

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    return r1, s1, t1


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

gcd, s, t = extended_euclid(x, y)
print("\nGCD =", gcd)
print("s1 =", s)
print("t1 =", t)


