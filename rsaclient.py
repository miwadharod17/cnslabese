import socket

# RSA decrypt
def rsa_decrypt(c, d, n):
    return pow(c, d, n)

# RSA private key
n = 3233
d = 2753   # modular inverse of e (17)

client = socket.socket()
client.connect(("127.0.0.1", 5000))

# Send message to server
msg = "HELLO"
client.send(msg.encode())

# Receive encrypted data
data = client.recv(1024).decode()
cipher_list = [int(x) for x in data.split(",")]

# Decrypt each number -> char
plain = "".join(chr(rsa_decrypt(c, d, n)) for c in cipher_list)

print("Original sent:", msg)
print("Received cipher:", cipher_list)
print("Decrypted text:", plain)

client.close()
