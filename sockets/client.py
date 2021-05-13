import socket
import time 

# host = socket.gethostname()
# host = "127.0.1.1"#
host = "10.0.0.98"
port = 12345

# print(host)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((host, port))
# s.sendall(b'Hello, world')
# data = s.recv(1024)
# s.close()
# print('Received', data.decode("utf-8"))

s = socket.socket()
s.settimeout(5)
s.connect((host, port))
for i in range(100):
    time.sleep(0.5)
    s.send(b"test")
s.close()