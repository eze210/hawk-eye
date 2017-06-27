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
											updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
											latitude DECIMAL(9,6),
											longitude DECIMAL(9,6)
											)''')
		self.conn.commit()

	def insertToFacebank(self, latitude, longitude):
		cursor = self.conn.cursor()
		cursor.execute("INSERT INTO faceBank (latitude, longitude) VALUES (" + str(latitude) + ", " + str(longitude) + ")")
		self.conn.commit()

	def closeDB(self):
		self.conn.close()