import os
import SocketServer
from ComputerVision.FaceComparator import FaceComparator
from ComputerVision.CV2Wrapper import CV2Wrapper


class FaceRecognizeTCPHandler(SocketServer.BaseRequestHandler):
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

        faceComparator = FaceComparator()
        openCV = CV2Wrapper()
        
        try:
            while True:
                # receives the cordinates from the CMB
                cordinates = self._readCordinates()

                # receives the timestamp
                timestamp = self._readTimestamp()

                # receives the number of images to receive
                numberOfImages = self._readLength()

                for x in xrange(0, numberOfImages):
                    # receives the length of an image
                    length = self._readLength()

                    # receives the image
                    self._readAll(length)

                    for root, dirs, files in os.walk("./templates"):
                        for fileName in files:
                            templateImage = openCV.imageRead("%s/%s" % (root, fileName))
                            receivedImage = openCV.imageFromBinary(self.data)
                            if faceComparator.facesCompare(templateImage, receivedImage):
                                # saves the images
                                with open('output/%s_%s.%d.jpg' % (cordinates, timestamp, x), 'wb') as f:
                                    f.write(self.data)
                                print "Image %d was saved" % x
                                print "MATCH"
                            else:
                                print "NO MATCH"

        except Exception as e:
            with open('output/exception.jpg', 'wb') as f:
                f.write(self.data)

            print "Connection with some neighborhood was lost: ", e
            raise e


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
