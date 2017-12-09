import werkzeug, os, sys, base64
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

import Database.DBWrapper as db
import ComputerVision.CV2Wrapper as cv2wrapper
import ComputerVision.FaceDetector as faceDetector
import ComputerVision.FaceComparator as faceComparator
import ComputerVision.FaceRecognizer as faceRecognizer
import datetime

dbw = db.DBWrapper()
app = Flask(__name__)
api = Api(app)

parserUpload = reqparse.RequestParser()
parserUpload.add_argument('uploadFile', type=werkzeug.datastructures.FileStorage, location='files')
parserUpload.add_argument('name')
parserUpload.add_argument('typeId')

class LocationHistorySRPL(Resource):
    def get(self, face_id):
        result = dbw.getLocationsOf(face_id)
        result = list(map(lambda x: (float(x[0]), float(x[1]), x[2].strftime("%Y-%m-%d %H:%M:%S")), result))
        return { 'data': result}, 200, {'Access-Control-Allow-Origin': '*'}
        
class FaceBankPost(Resource):
    def options(self):
        return {'Allow' : 'POST' }, 200, \
               { 'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods' : 'PUT,GET' }
    def post(self):
        args = parserUpload.parse_args()
        name = args['name']
        typeId = args['typeId']
        print 'Type Identifier: ', typeId
        if typeId == '0':
            path = os.getcwd() + "/RestAPI/SRPL/" + args['uploadFile'].filename
        else:
            path = os.getcwd() + "/RestAPI/SRE/" + args['uploadFile'].filename
        print 'Saving path: %s\n' % path
        args['uploadFile'].save(path)
        faced = faceDetector.FaceDetector()
        cv2 = cv2wrapper.CV2Wrapper()
        with open(path, "rb") as image_file:
            data = image_file.read()
        faces = []
        faces = faces + [cv2.imageToBinary(face) for face in faced.detectFromBinary(data)]
        print "Detected %d faces" % len(faces)
        ids = []
        number = 1
        for found in faces:
            filename = 'RestAPI/SRPL/%s_%d.jpg' % (args['uploadFile'].filename, number)
            with open(filename, 'wb') as f:
                f.write(found)
            lastId = dbw.insertNewFaceImage(name, os.getcwd() + '/' + filename, typeId)
            ids.append(lastId)
            number = number + 1
        os.remove(path)
        return {'ids': ids}, 201, {'Access-Control-Allow-Origin': '*'}

class FaceBank(Resource):
    def get(self, type_id):
        result = dbw.getFaces(type_id)
        i = 0
        for var in result:
            with open(var[1], "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            new = (str(var[0]), encoded_string, var[2])
            result[i] = new
            i += 1
        return { 'data': result}, 200, {'Access-Control-Allow-Origin': '*'}


class SearchFaceBankSRPL(Resource):
    def options(self):
        return {'Allow' : 'POST' }, 200, \
                { 'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods' : 'PUT,GET' }
    def post(self):
        args = parserUpload.parse_args()
        uploadFile = args['uploadFile']
        typeIdentifier = args['typeId']
        faced = faceDetector.FaceDetector()
        faceComp = faceComparator.FaceComparator()

        recognizer = faceRecognizer.FaceRecognizer()

        cv2 = cv2wrapper.CV2Wrapper()
        facesInQuery = [cv2.toGrayScale(face) for face in faced.detectFromBinary(uploadFile.read())]
        print "Detected %d faces in query" % len(facesInQuery)
        result = dbw.getFaces(typeIdentifier)

        facesInDB = [cv2.toGrayScale(cv2.imageRead(r[1])) for r in result]
        namesInDB = [r[2] for r in result]
        noRepeat = list(set(namesInDB))
        labels = [noRepeat.index(name) for name in namesInDB]
        recognizer.train(facesInDB, labels)

        predicted = []
        for f in facesInQuery:
            (predictLabel, predictDistance) = recognizer.predict(f)
            predictName = noRepeat[predictLabel]
            print "Predict %s with distance %f" % (predictName, predictDistance)
            if predictDistance < 20:
                predicted.append(predictName)

        matches = []
        for i in range(len(facesInDB)):
            if namesInDB[i] in predicted:
                print "Found a MATCH in search\n"
                with open(result[i][1], "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                new = (result[i][0], encoded_string, namesInDB[i])
                matches.append(new)
        return {'matches': matches}, 201, {'Access-Control-Allow-Origin': '*'}

api.add_resource(FaceBank, '/faces/<type_id>')
api.add_resource(FaceBankPost, '/faces')
api.add_resource(SearchFaceBankSRPL, '/search')
api.add_resource(LocationHistorySRPL, '/locations/srpl/<face_id>')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        app.run(host= sys.argv[1], port=sys.argv[2])
    else:
        raise RuntimeError("Invalid parameters")
