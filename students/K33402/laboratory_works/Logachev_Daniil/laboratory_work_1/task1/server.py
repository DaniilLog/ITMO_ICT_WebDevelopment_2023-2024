import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 3000)
server_socket.bind(server_address)

print('Server is on. Waiting for messages...')

while True:
    message, client_address = server_socket.recvfrom(1024)

    print(
        f'Got a message from a client {client_address}: {message.decode()}')

    response = 'Hello, client!'
    server_socket.sendto(response.encode(), client_address)