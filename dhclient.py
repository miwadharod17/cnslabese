import socket
import random

s = socket.socket()
s.connect(("127.0.0.1", 5000))

# Receive p, g, A from server
data = s.recv(1024).decode()
p, g, A = map(int, data.split(","))

# Client private key
b = random.randint(1, p-2)
B = pow(g, b, p)      # g^b mod p

# Send B to server
s.send(str(B).encode())

# Compute shared secret
shared_key = pow(A, b, p)

print("Shared secret =", shared_key)

# Receive confirmation from server
print("Server replied:", s.recv(1024).decode())

s.close()
