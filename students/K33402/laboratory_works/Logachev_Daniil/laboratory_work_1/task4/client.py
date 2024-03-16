import socket
import threading

# Указываем адрес сервера и порт
server_address = ('localhost', 3003)

# Создаем клиентский соксет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем соединение с сервером
client_socket.connect(server_address)

# Функция для приема сообщений от сервера
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            break

# Создаем поток для приема сообщений
receive_thread = threading.Thread(target=receive_messages)

# Запускаем поток
receive_thread.start()

# Основной цикл для отправки сообщений
while True:
    # Получаем сообщение от пользователя
    message = input()
    # Кодируем сообщение в байты с использованием кодировки UTF-8 и отправляем на сервер
    client_socket.send(message.encode('utf-8'))