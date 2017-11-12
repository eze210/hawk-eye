import psycopg2 as dbModule
import time

class DBWrapper(object):

	def __init__(self,
				 dbPath = '/tmp/TrackingCollection.db'):

		#self.conn = dbModule.connect(dbPath)
		self.conn = dbModule.connect(database='tracking', user='maxroach', host='localhost', port=26257)
		self.conn.set_session(autocommit=True)
		self.typeSRPL = 0
		self.typeSRE = 1

	def createBaseTables(self):
		cursor = self.conn.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS faceBank
											(id SERIAL PRIMARY KEY,
											created_at TIMESTAMPTZ,
											name TEXT,
											imagePath TEXT,
											type INTEGER
											)''')


		cursor.execute('''CREATE TABLE IF NOT EXISTS locationHistory
											(id SERIAL PRIMARY KEY,
											face_id INTEGER,
											created_at TIMESTAMPTZ,
											latitude DECIMAL(9,6),
											longitude DECIMAL(9,6),
											FOREIGN KEY (face_id) REFERENCES faceBank(id)
											)''')
		
		self.conn.commit()

	def getFaces(self, typeId):
		cursor = self.conn.cursor()
		cursor.execute("select id, imagePath, name from faceBank WHERE type = " + str(typeId) +";")
		return cursor.fetchall()

	def getFacesPaths(self):
		cursor = self.conn.cursor()
		cursor.execute("select id, imagePath, name from faceBank;")
		return cursor.fetchall()

	def insertLocationTrace(self, face_id, latitude, longitude):
		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO locationHistory (face_id, latitude, longitude) VALUES (" + str(face_id) + ", " + str(latitude) + ", " + str(longitude) + ")")
		self.conn.commit()
		return cursor.lastrowid

	def getLocationsOf(self, face_id):
		cursor = self.conn.cursor()
		cursor.execute("SELECT latitude, longitude FROM locationHistory WHERE face_id = %s;" % face_id)
		return cursor.fetchall()

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


# db = DBWrapper()
# db.createBaseTables()