import SocketServer
import socket, fcntl, struct

def _get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client

        # receives the number of images to receive
        numberOfImages = self._readLength()

        for x in xrange(0,numberOfImages):
            # receives the length of an image
            length = self._readLength()
            # receives the image
            self._readAll(length)
    
            # saves the image
            f = open('out_%d.%s.jpg' % (x, self.client_address[0]), 'w')
            f.write(self.data)
            f.close()
    
            # just send ok
            self.request.sendall('ok')

    def _readLength(self):
        rv = 0
        while True:
            readed = self.request.recv(1)
            if readed == '\n':
                return rv
            else:
                rv = rv * 10 + int(readed)

    def _readAll(self, length):
        self.data = self.request.recv(length)
        while len(self.data) < length:
            self.data += self.request.recv(length - len(self.data))


if __name__ == "__main__":
    HOST, PORT = _get_ip_address('eth0'), 9998
    f = open('./raspy/ip.temp', 'w')
    f.write('%s%c%d' % (HOST, '\n', PORT))
    f.close()

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
