import sqlite3
import time

class DBWrapper(object):

	def __init__(self,
				 dbPath = '/tmp/TrackingCollection.db'):

		self.conn = sqlite3.connect(dbPath)
		self.typeSRPL = 0
		self.typeSRE = 1

	def createBaseTables(self):
		cursor = self.conn.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS faceBank
											(id INTEGER PRIMARY KEY AUTOINCREMENT,
											created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
											name TEXT,
											imagePath TEXT,
											siftPath TEXT,
											type INTEGER
											)''')

		cursor.execute('''CREATE TABLE IF NOT EXISTS locationHistory
											(id INTEGER PRIMARY KEY AUTOINCREMENT,
											face_id INTEGER
											created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
											latitude DECIMAL(9,6),
											longitude DECIMAL(9,6),
											FOREIGN KEY (face_id) REFERENCES faceBank(id)
											)''')
		
		self.conn.commit()

	def getFaces(self, typeId):
		cursor = self.conn.cursor()
		self.conn.text_factory = str
		query = cursor.execute("select id, imagePath, name from faceBank WHERE type = " + str(typeId) +";")
		return query.fetchall()

	def getFacesPaths(self):
		cursor = self.conn.cursor()
		self.conn.text_factory = str
		query = cursor.execute("select id, imagePath from faceBank;")
		return query.fetchall()

	def insertLocationTrace(self, face_id, latitude, longitude):
		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO locationHistory (face_id, latitude, longitude) VALUES (" + str(face_id) + ", " + str(latitude) + ", " + str(longitude) + ")")
		self.conn.commit()
		return cursor.lastrowid

	def getLocationsOf(self, face_id):
		cursor = self.conn.cursor()
		self.conn.text_factory = str
		query = cursor.execute("SELECT latitude, longitude FROM locationHistory WHERE face_id = %s;" % face_id)
		return query.fetchall()				

	def insertNewFaceImage(self, name, imagePath, typeUp):
		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO faceBank (name, imagePath, type) VALUES ('" + name + "', '" + imagePath + "', '" + str(typeUp) + "')")
		self.conn.commit()
		return cursor.lastrowid

	# def addPattern(self, id, mtxs):
	# 	# print "Save PK:<%s>\nMatrices:" % str(id)
	# 	# print mtxs
	# 	cursor = self.conn.cursor()
	# 	cursor.execute("UPDATE faceBa-nk SET siftPath = '" + mtxs + "' WHERE id = " + str(id))

	def closeDB(self):
		self.conn.close()


db = DBWrapper()
db.createBaseTables()