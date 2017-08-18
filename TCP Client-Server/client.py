# import socket

# TCP_IP= '127.0.01'
# TCP_PORT= 5005
# BUFFER_SIZE  = 1024

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((TCP_IP, TCP_PORT))
# s.send("Hello")
# data=s.recv(BUFFER_SIZE)
# s.close()
# print(data)

import socket
host='127.0.1.1'
print host
port = 5060
buffer_size= 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
    command = input("Enter your command: ")
    if command == 'EXIT':
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        print "SENDING KILL"
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply=s.recv(buffer_size)
    print(reply.decode('utf-8'))
s.close()
