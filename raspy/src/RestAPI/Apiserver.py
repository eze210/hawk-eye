from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///../Database/TrackingCollection.db')
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

class FaceBank(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select name, imageUrl from faceBank;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class LocationHistory(Resource):
    def get(self, face_id):
        conn = db_connect.connect()
        query = conn.execute("select * FROM locationHistory WHERE id = %d " %int(face_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(FaceBank, '/faces')
api.add_resource(LocationHistory, '/locations/<face_id>')


if __name__ == '__main__':
     app.run(port='5002')
     
There will be thre