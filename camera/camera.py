import socket
import sys

def _read_ip_from_temp():
    f = open('../raspy/ip.temp', 'r')
    ip = f.readline()
    port = int(f.readline())
    f.close()
    return ip, port


HOST, PORT = _read_ip_from_temp()
IM_NAMES = sys.argv[1:]

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    # Sends the number of images as string
    sock.sendall('%d\n' % len(IM_NAMES))

    for imageName in IM_NAMES:
        # Reads all the image
        f = open(imageName, 'r')
        # When read() does not receive a length, it reads the whole file
        data = f.read()
        f.close()
    
        # Sends the length as string
        sock.sendall('%d\n' % len(data))
        # Sends the data
        sock.sendall(data)
    
        # Receive ok from the server and shut down
        received = sock.recv(1024)
        print received
finally:
    sock.close()
