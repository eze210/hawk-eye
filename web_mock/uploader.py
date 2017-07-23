#usage: python uploader.py name img0.jpg img1.jpg img2.jpg ... imgN.jpg

import socket
import sys
import datetime
import time


def _read_ip_from_temp():
    f = open('../raspy/ip.city.temp', 'r')
    ip = f.readline()
    port = 9991
    f.close()
    return ip, port


HOST, PORT = _read_ip_from_temp()
FACE_NAME = sys.argv[1]
IM_NAMES = sys.argv[2:]

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    print 'Trying to connect to %s:%d' % (HOST, PORT)
    sock.connect((HOST, PORT))

    # Sends command
    sock.sendall('ADD\n')

    # Sends name of person
    sock.sendall('%s\n' % FACE_NAME)

    # Sends the number of images as string
    sock.sendall('%d\n' % len(IM_NAMES))

    for imageName in IM_NAMES:
        # Reads all the image
        with open(imageName, 'rb') as f:
            # When read() does not receive a length, it reads the whole file
            data = f.read()
    
        # Sends the length as string
        sock.sendall('%d\n' % len(data))
        # Sends the data
        sock.sendall(data)
    
    # Receive ok from the server and shut down
    received = sock.recv(1024)
    print received

finally:
    sock.close()
