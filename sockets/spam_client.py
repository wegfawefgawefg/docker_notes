import socket
import time 

host = "10.0.0.98"
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)
    s.connect((host, port))
    for i in range(10):
        time.sleep(0.01)
        s.send(str(i).encode())
