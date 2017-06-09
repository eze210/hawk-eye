import socket
import sys

def _read_ip_from_temp():
    f = open('ip.temp', 'r')
    ip = f.readline()
    port = int(f.readline())
    f.close()
    return ip, port


HOST, PORT = _read_ip_from_temp()
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)