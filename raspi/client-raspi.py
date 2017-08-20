import socket
import io
import struct
import time
import picamera



host='192.168.43.30'
#host ='0.0.0.0'
print(host)
port = 5060
port = 8000
buffer_size= 1024



# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

# Make a file-like object out of the connection
connection = s.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30
        # Start a preview and let the camera warm up for 2 seconds
        camera.start_preview()
        time.sleep(2)

        # Note the start time and construct a stream to hold image data
        # temporarily (we could write it directly to connection but in this
        # case we want to find out the size of each capture first to keep
        # our protocol simple)
        start = time.time()
        stream = io.BytesIO()
        
        for foo in camera.capture_continuous(stream, 'jpeg' , use_video_port = True):
            # Write the length of the capture to the stream and flush to
            # ensure it actually gets sent
            
            connection.write(struct.pack('<L', stream.tell()))
            
            connection.flush()
            print "HERE"
            #time.sleep(2)
            # Rewind the stream and send the image data over the wire
            stream.seek(0)
            connection.write(stream.read())
            
            # If we've been capturing for more than 30 seconds, quit
            if time.time() - start > 30:
                break
            # Reset the stream for the next capture
            stream.seek(0)
            stream.truncate()
    # Write a length of zero to the stream to signal we're done
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    s.close()
