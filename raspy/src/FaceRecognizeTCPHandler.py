import os
import SocketServer
from ComputerVision.FaceComparator import FaceComparator
from ComputerVision.FaceRecognizer import FaceRecognizer
from ComputerVision.CV2Wrapper import CV2Wrapper
from Database.DBWrapper import DBWrapper

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
                print "%s" % cordinates
                # receives the timestamp
                timestamp = self._readTimestamp()
                # receives the number of images to receive
                numberOfImages = self._readLength()
                db = DBWrapper()
                recognizer = FaceRecognizer()
                result = db.getFacesPaths()

                facesInDB = [openCV.toGrayScale(openCV.imageRead(r[1])) for r in result]
                namesInDB = [r[2] for r in result]
                noRepeat = list(set(namesInDB))
                labels = [noRepeat.index(name) for name in namesInDB]
                recognizer.train(facesInDB, labels)

                facesIDs = {}
                for name in noRepeat:
                    facesIDs[name] = []
                
                for item in result:
                    facesIDs[item[2]].append(item[0])

                for x in xrange(0, numberOfImages):
                    # receives the length of an image
                    length = self._readLength()

                    # receives the image
                    self._readAll(length)

                    receivedImage = openCV.imageFromBinary(self.data)
                    
                    (predictLabel, predictDistance) = recognizer.predict(openCV.toGrayScale(receivedImage))
                    predictName = noRepeat[predictLabel]
                    print "Predict %s with distance %f" % (predictName, predictDistance)
                    if predictDistance < 20:
                        lat, longi = cordinates.split(",")
                        for faceID in facesIDs[predictName]:
                            print "Saving..."
                            db.insertLocationTrace(faceID, lat, longi, timestamp)
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
