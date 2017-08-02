import socket

TCP_IP= '127.0.01'
TCP_PORT= 5005
BUFFER_SIZE  = 1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send("Hello")
data=s.recv(BUFFER_SIZE)
s.close()
print(data)