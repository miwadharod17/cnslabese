import socket
import random

# Public parameters (can be shared)
p = 23              # prime
g = 5               # primitive root mod p

# Server private key
a = random.randint(1, p-2)
A = pow(g, a, p)    # g^a mod p

s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen(1)

print("Server waiting...")
conn, addr = s.accept()
print("Connected:", addr)

# Send p, g, A
conn.send(f"{p},{g},{A}".encode())

# Receive client's public key B
B = int(conn.recv(1024).decode())

# Shared secret = B^a mod p
shared_key = pow(B, a, p)

print("Shared secret =", shared_key)
conn.send(str(shared_key).encode())

conn.close()
s.close()
