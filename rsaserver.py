import socket

# Simple RSA functions
def rsa_encrypt(m, e, n):
    return pow(m, e, n)

# RSA keys (public)
n = 3233
e = 17

server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen(1)
print("Server waiting...")

conn, addr = server.accept()
print("Connected:", addr)

# Receive plaintext
text = conn.recv(1024).decode()

# Convert each char -> ASCII -> RSA encrypt
cipher = [str(rsa_encrypt(ord(ch), e, n)) for ch in text]
cipher_text = ",".join(cipher)   # send comma-separated integers

conn.send(cipher_text.encode())

conn.close()
server.close()
