import socket

server_address = ('localhost', 3002)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)

http_request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
client_socket.sendall(http_request.encode('utf-8'))

response = b""
while True:
    try:
        data = client_socket.recv(1024)
    except:
        break
    response += data

client_socket.close()

http_response = response.decode('utf-8')
header, html_content = http_response.split('\r\n\r\n', 1)

print(header)
print(html_content)