import SocketServer
from ComputerVision.FaceDetector import FaceDetector
from ComputerVision.CV2Wrapper import CV2Wrapper


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
        
        # receives the cordinates from the camera
        cordinates = self._readCordinates()
        print cordinates

        # receives the timestamp
        timestamp = self._readTimestamp()
        print timestamp

        # receives the number of images to receive
        numberOfImages = self._readLength()

        for x in xrange(0,numberOfImages):
            # receives the length of an image
            length = self._readLength()

            # receives the image
            self._readAll(length)

            facesAsStr = [openCV.imageToBinary(face) for face in faceDetector.detectFromBinary(self.data)]

            # saves the images
            faceIdx = 0
            for face in facesAsStr:
                faceIdx += 1
                with open('output/%d_%d.%s.jpg' % (x, faceIdx, self.client_address[0]), 'wb') as f:
                    f.write(face)

            # just send ok
            self.request.sendall('ok')


    def _readCordinates(self):
        return self._readLine()


    def _readTimestamp(self):
        return self._readLine()


    def _readLine(self):
        rv = ''
        while True:
            readed = self.request.recv(1)
            if readed == '\n':
                return rv
            else:
                rv = rv + readed


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
