from ThreadedTCPServer import ThreadedTCPServer
from FaceCropTCPHandler import FaceCropTCPHandler
import socket


class NeighborhoodMonitorCenter(ThreadedTCPServer):
	"""NeighborhoodMonitorCenter (Centro de Monitoreo Barrial)"""

	def __init__(self, *args, **kwargs):
		HOST, PORT = args[0][1][0], args[0][1][1]
		args = args[0] + (FaceCropTCPHandler,)
		ThreadedTCPServer.__init__(self, *args, **kwargs)
		
		# Create a socket (SOCK_STREAM means a TCP socket)
		self.socketToCity = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socketToCity.connect((HOST, PORT))	
