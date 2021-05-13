import socket
import time

host = ''
port = 12345

while True:
    print("...awaiting connnection")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"Connection: {addr}")
            while True:
                data = conn.recv(1024)
                if not data: 
                    break
                msg = data.decode('utf-8')
                print(f"msg: {msg}")
    print(f"{addr} conn closed")
