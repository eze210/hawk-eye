import sqlite3


class DBWrapper(object):

	def __init__(self,
				 dbPath = 'TrackingCollection.db'):

		# self.dbPath = dbPath;
		self.conn = sqlite3.connect(dbPath)


	# Still need to define what we are gonna save about image comparison
	def createBaseTables(self):
		cursor = self.conn.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS faceBank
											(id INTEGER PRIMARY KEY AUTOINCREMENT,
											created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
											name TEXT,
											imageUrl TEXT
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


	def insertLocationTrace(self, face_id, latitude, longitude):
		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO locationHistory (face_id, latitude, longitude) VALUES (" + str(face_id) + ", " + str(latitude) + ", " + str(longitude) + ")")
		self.conn.commit()


	def addPattern(self, personName, mtxs):
		print "Save PK:<%s>\nMatrices:" % personName
		print mtxs


	def closeDB(self):
		self.conn.close()