# 客户端代码
import socket
import threading

SERVER_HOST = '192.168.196.246'  # 服务器端IP地址
SERVER_PORT = 65432        # 端口号，需要与服务器端一致

def receive_message(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    threading.Thread(target=receive_message, args=(s,)).start()

    while True:
        message = input('Enter message to send: ')
        s.sendall(message.encode())