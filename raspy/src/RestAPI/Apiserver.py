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

# db_connect = create_engine('sqlite:///tmp/TrackingCollection.db')
app = Flask(__name__)
api = Api(app)

parserUpload = reqparse.RequestParser()
parserUpload.add_argument('photo', type=werkzeug.datastructures.FileStorage, location='files')

class FaceBankSRPL(Resource):
    def get(self):
        # conn = db_connect.connect()
        # query = conn.execute("select imagePath from faceBank WHERE type = 0;")
        # result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        result = dbw.getFaces(0)
        return jsonify(result)

class LocationHistory(Resource):
    def get(self, face_id):
        # conn = db_connect.connect()
        # query = conn.execute("select * FROM locationHistory WHERE face_id = %d " %int(face_id))
        # result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        result = dbw.getLocationHistory(face_id)
        return jsonify(result)
        
class FaceBankUploadSRPL(Resource):
    def options(self):
        return {'Allow' : 'POST' }, 200, \
               { 'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods' : 'PUT,GET' }
    def post(self):
        args = parserUpload.parse_args()
        path = os.getcwd() + "/SRPL/" + args['photo'].filename
        args['photo'].save(path);
        dbw.insertNewFaceImage(path, 0)
        return {'success': args['photo'].filename}, 201, {'Access-Control-Allow-Origin': '*'}

api.add_resource(FaceBankSRPL, '/faces/srpl')
api.add_resource(FaceBankUploadSRPL, '/faces/uploadsrpl')
api.add_resource(LocationHistory, '/locations/<face_id>')


if __name__ == '__main__':
     app.run(port='5002')