import socket
import io
import struct
import time
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os
import math
from IPython.display import clear_output
import time
import pyautogui
import cv2


host = socket.gethostbyname(socket.gethostname())
#host='0.0.0.0'
print host
port = 8000
#port = 5060
buffer_size = 1024


# Define a function to display image using numpy
def plt_showImage(image, title=""):
    #if len(image.shape) == 3   : # 3 channels
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.axis("off")
    plt.title(title)
    plt.imshow(image, cmap="Greys_r")
    plt.show()


# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(0)


def plt_showImage(image, title=""):
    #if len(image.shape) == 3   : # 3 channels
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.axis("off")
    plt.title(title)
    plt.imshow(image, cmap="Greys_r")
    plt.show()




connection = server_socket.accept()[0].makefile('rb')
try:
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = np.array(Image.open(image_stream))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imshow('window', image)
        #print image
        #plt_showImage(image)
        clear_output(wait=True) # wait for the new op
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
        print('Image is %dx%d' % Image.open(image_stream).size)
        Image.open(image_stream).verify()
        print('Image is verified')
finally:
    connection.close()
    server_socket.close()   
