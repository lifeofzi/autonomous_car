# import socket

# TCP_IP= '127.0.01'
# TCP_PORT= 5005
# BUFFER_SIZE  = 1024

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(1)

# conn, addr = s.accept()
# while 1:
#   data = conn.recv(BUFFER_SIZE)
#   if not data: break
#   print "received data:", data
#   conn.send(data)  # echo
# conn.close()

import socket
#host = '127.0.0.1'
host = socket.gethostbyname(socket.gethostname())
print host
port = 5060
buffer_size = 1024

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket Created"
    try:
        s.bind((host,port))
    except socket.error as msg:
        print (msg)
    print "Socket Bind complete"
    return s

def setupConnection():
    s.listen(1) # HOW MANY PEOPLE , here one connection at a time
    conn, address = s.accept()
    print("Connected to:" + address[0] + ":" + str(address[1]))
    return conn

def GET():
    reply = "YO !"
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply


def dataTransfer(conn):
    # A big loop that sends/recieves data until told not to
    while True:
        # Recieve the data
        data = conn.recv(buffer_size) #recv
        data = data.decode('utf-8') # decode in strings
        #split
        dataMessage = data.split(' ' , 1)
        command  = dataMessage[0]
        if command == 'GET' :
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Our client has left us :'( ")
            break
        elif command == 'KILL':
            print("Server Shutting down")
            s.close()
            break
        else:
            reply = 'Unknown Command'
        conn.sendall(str.encode(reply))
        print("data has been sent !")
    conn.close()


s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
        
    except:
        print "Except Block reached"
        break
        
        

















