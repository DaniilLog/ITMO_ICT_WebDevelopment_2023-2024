import socket

server_address = ('localhost', 3002)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen(100)

print(f"Server is on {server_address[0]}:{server_address[1]}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(html_content)}\r\n\r\n{html_content}"
    client_socket.sendall(response.encode('utf-8'))

    client_socket.close()