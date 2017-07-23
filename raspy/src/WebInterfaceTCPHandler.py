import os
import SocketServer

from ComputerVision.FaceDetector import FaceDetector
from ComputerVision.CV2Wrapper import CV2Wrapper
from Database.DBWrapper import DBWrapper


class WebInterfaceTCPHandler(SocketServer.BaseRequestHandler):
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
        db = DBWrapper()

        # receives the command name
        command = self._readCommand()

        if command == 'ADD':
            # receives the person name
            personName = self._readName()
    
            # receives the number of images to receive
            numberOfImages = self._readLength()
    
            faces = []
            for x in xrange(0, numberOfImages):
                # receives the length of an image
                length = self._readLength()

                # receives the image
                self._readAll(length)

                faces = faces + [face for face in faceDetector.detectFromBinary(self.data)]
                print "Detected %d faces" % len(faces)

            db.addPattern(personName, [openCV.toSIFTMatrix(face) for face in faces])

        self.request.sendall('ok')


    def _readCommand(self):
        return self._readLine()


    def _readName(self):
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

