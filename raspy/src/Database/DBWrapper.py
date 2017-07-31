import sqlite3
import time

class DBWrapper(object):

	def __init__(self,
				 dbPath = '/tmp/TrackingCollection.db'):

		# self.dbPath = dbPath;
		self.conn = sqlite3.connect(dbPath)
		self.typeSRPL = 0
		self.typeSRE = 1

	# Still need to define what we are gonna save about image comparison
	def createBaseTables(self):
		cursor = self.conn.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS faceBank
											(id INTEGER PRIMARY KEY AUTOINCREMENT,
											created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
											-- name TEXT,
											imagePath TEXT,
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
		query = cursor.execute("select id as id, imagePath as image from faceBank WHERE type = " + str(typeId) +";")
		return query.fetchall()

	def insertLocationTrace(self, face_id, latitude, longitude):
		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO locationHistory (face_id, latitude, longitude) VALUES (" + str(face_id) + ", " + str(latitude) + ", " + str(longitude) + ")")
		self.conn.commit()

	def insertNewFaceImage(self, imagePath, typeUp):
		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO faceBank (imagePath, type) VALUES ('" + imagePath + "', " + str(typeUp) + ")")
		self.conn.commit()


	def addPattern(self, personName, mtxs):
		print "Save PK:<%s>\nMatrices:" % personName
		print mtxs


	def closeDB(self):
		self.conn.close()


db = DBWrapper()
db.createBaseTables()