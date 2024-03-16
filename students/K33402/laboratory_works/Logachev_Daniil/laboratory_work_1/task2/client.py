import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 3001))
data = input("Enter a, b, c - coefficients of equation: ")
client.send(bytes(data, "utf-8"))

full_msg = ""

while True:
    msg = client.recv(1024)

    if len(msg) <= 0:
        break

    full_msg += msg.decode("utf-8")

print(full_msg)