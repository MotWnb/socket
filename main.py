# 服务器端代码
import socket
import threading

HOST = '192.168.196.246'  # 本地主机IP地址
PORT = 65432        # 端口号，可以自定义

def handle_client(conn, addr):
    print(f'Connected by {addr}')

    def receive_message():
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'Received from {addr}: {data.decode()}')

    threading.Thread(target=receive_message).start()

    while True:
        message = input('Enter message to send: ')
        conn.sendall(message.encode())

    conn.close()
    print(f'Connection closed by {addr}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server is running on {HOST}:{PORT}')

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
