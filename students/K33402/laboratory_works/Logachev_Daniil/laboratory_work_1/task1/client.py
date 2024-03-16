import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 3000)

message = 'Hello, server!'
client_socket.sendto(message.encode(), server_address)

response, _ = client_socket.recvfrom(1024)

print(f'Answer from server: {response.decode()}')

client_socket.close()