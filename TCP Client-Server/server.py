import socket

TCP_IP= '127.0.01'
TCP_PORT= 5005
BUFFER_SIZE  = 1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
while 1:
  data = conn.recv(BUFFER_SIZE)
  if not data: break
  print "received data:", data
  conn.send(data)  # echo
conn.close()