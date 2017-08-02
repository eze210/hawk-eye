import werkzeug
import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import imp
db = imp.load_source('DBWrapper', '../Database/DBWrapper.py')
dbw = db.DBWrapper()
import base64

# db_connect = create_engine('sqlite:///tmp/TrackingCollection.db')
app = Flask(__name__)
api = Api(app)

parserUpload = reqparse.RequestParser()
parserUpload.add_argument('uploadFile', type=werkzeug.datastructures.FileStorage, location='files')
parserUpload.add_argument('name')

class LocationHistory(Resource):
    def get(self, face_id):
        # conn = db_connect.connect()
        # query = conn.execute("select * FROM locationHistory WHERE face_id = %d " %int(face_id))
        # result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        result = dbw.getLocationHistory(face_id)
        return jsonify(dict(result))
        
class FaceBankSRPL(Resource):
    def options(self):
        return {'Allow' : 'POST' }, 200, \
               { 'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods' : 'PUT,GET' }
    def post(self):
        args = parserUpload.parse_args()
        path = os.getcwd() + "/SRPL/" + args['uploadFile'].filename
        args['uploadFile'].save(path);
        name = args['name']
        lastId = dbw.insertNewFaceImage(name, path, 0)
        return {'id': lastId}, 201, {'Access-Control-Allow-Origin': '*'}
    
    def get(self):
        result = dbw.getFaces(0)
        i = 0
        for var in result:
            with open(var[1], "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            new = (var[0], encoded_string, var[2])
            result[i] = new
            i += 1
        return { 'data': result}, 200, {'Access-Control-Allow-Origin': '*'}

api.add_resource(FaceBankSRPL, '/faces/srpl')
api.add_resource(LocationHistory, '/locations/<face_id>')


if __name__ == '__main__':
     app.run(host= '192.168.1.112', port='5002')