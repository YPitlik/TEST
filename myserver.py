import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5000
server_socket.bind((host, port))


server_socket.listen()

print(f"Сервер запущен  ...")


client_socket, client_address = server_socket.accept()
print(f"Клиент  подключился к серверу.")


