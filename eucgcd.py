def gcd(a, b):
    r1, r2 = a, b
    print("q\t r1\t r2\t r")
    
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        print(f"{q}\t {r1}\t {r2}\t {r}")
        r1, r2 = r2, r
    return r1

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD =", gcd(x, y))
