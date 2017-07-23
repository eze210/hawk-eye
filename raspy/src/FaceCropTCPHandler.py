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
        
#        try:
        if True:
            while True:
                # receives the cordinates from the camera
                cordinates = self._readCordinates()
        
                # receives the timestamp
                timestamp = self._readTimestamp()
        
                # receives the number of images to receive
                numberOfImages = self._readLength()
        
                facesAsStr = []
                for x in xrange(0, numberOfImages):
                    # receives the length of an image
                    length = self._readLength()
        
                    # receives the image
                    self._readAll(length)
        
                    facesAsStr = facesAsStr + [openCV.imageToBinary(face) for face in faceDetector.detectFromBinary(self.data)]
                    print "Detected %d faces" % len(facesAsStr)
        
                self.server.socketToCity.sendall("%s\n" % cordinates)
                self.server.socketToCity.sendall("%s\n" % timestamp)
                self.server.socketToCity.sendall("%d\n" % len(facesAsStr))
    
                # sends the images
                for face in facesAsStr:
                    self.server.socketToCity.sendall("%d\n" % len(face))                
                    self.server.socketToCity.sendall(face)

                self.request.sendall('ok')

#        except Exception as e:
#            print "Connection with some camera was lost"


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
