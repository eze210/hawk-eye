import socket, fcntl, struct,  threading
from CityMonitorCenter import CityMonitorCenter
from WebInterfaceServer import WebInterfaceServer


def _get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


if __name__ == "__main__":
    HOST, PORT, PORT_WEB = _get_ip_address('eth0'), 9990, 9991
    #HOST, PORT = 'localhost', 9990

    with open('./ip.city.temp', 'w') as f:
        f.write('%s%c%d' % (HOST, '\n', PORT))

    # Create the server, binding to localhost on port 9990
    faceRecognizerServer = CityMonitorCenter((HOST, PORT))

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    serverThread = threading.Thread(target=faceRecognizerServer.serve_forever)
    # Exit the server thread when the main thread terminates
    serverThread.daemon = True
    serverThread.start()

    # Create the other server (comm with web), binding to localhost on port 9991
    webInterfaceServer = WebInterfaceServer((HOST, PORT_WEB))

    # Activate it; this will keep running until you
    # interrupt the program with Ctrl-C
    webInterfaceServer.serve_forever()

    faceRecognizerServer.shutdown()
    faceRecognizerServer.server_close()
