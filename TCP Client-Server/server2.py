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
print host
port = 8000
buffer_size = 1024


# -------------------------------------Define a function to display image using numpy--(For Jupyter Notebooks )----------------------------
def plt_showImage(image, title=""):
    if len(image.shape) == 3   : # 3 channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.axis("off")
    plt.title(title)
    plt.imshow(image, cmap="Greys_r")
    plt.show()

#-------------------------------------------------NORMALIZE IMAGE------------------------------------------------------
def normalize_image(image):
    return image
    ## CODE CODE
    
    
#--------------------------------------------CREATING OUR DATA SET----------------------------------------------------   
def collect_Images(images,direction,counter):
    folder = "C:\Users\Carpe\Desktop\Game\ " + str(direction)
    image_nm = normalize_image(image)
    if not os.path.exists(folder):
        os.mkdir(folder)  #creates direc named after the person
        cv2.imwrite(folder + '\ ' + str(counter) + '.jpg', image_nm)
        counter=counter+1
    else:
        for i , im  in enumerate(os.listdir(folder)):
            counter=i+1
        cv2.imwrite(folder + '\ ' + str(counter) + '.jpg', image_nm)   
        counter=counter+1
    return counter
# ----------------------------Start a socket listening for connections on 'your host name':8000------------------------------------
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(0)





connection = server_socket.accept()[0].makefile('rb')
try:
    counter = 0
    direction = raw_input('Direction: ').lower()
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        
        # Rewind the stream, open it as an image with PIL and do some processing on it
        image_stream.seek(0)
        image = np.array(Image.open(image_stream))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imshow('window', image)
        counter=collect_Images(image,direction,counter)
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
