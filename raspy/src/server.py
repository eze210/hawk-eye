import SocketServer
import socket, fcntl, struct
from ComputerVision.FaceDetector import FaceDetector
from ComputerVision.CV2Wrapper import CV2Wrapper


def _get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


class FaceCropTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def __init__(self, *args, **kwargs):
        SocketServer.BaseRequestHandler.__init__(self, *args, **kwargs)


    def handle(self):
        # self.request is the TCP socket connected to the client

        faceDetector = FaceDetector()
        openCV = CV2Wrapper()
        
        # receives the number of images to receive
        numberOfImages = self._readLength()

        for x in xrange(0,numberOfImages):
            # receives the length of an image
            length = self._readLength()
            
            # receives the image
            self._readAll(length)

            facesAsStr = [openCV.imageToBinary(face) for face in faceDetector.detectFromBinary(self.data)]

            # saves the images
            face_idx = 0
            for face in facesAsStr:
                face_idx += 1
                with open('output/%d_%d.%s.jpg' % (x, face_idx, self.client_address[0]), 'wb') as f:
                    f.write(face)
    
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
    HOST, PORT = _get_ip_address('eth0'), 9999

    with open('./ip.temp', 'w') as f:
        f.write('%s%c%d' % (HOST, '\n', PORT))

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), FaceCropTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
