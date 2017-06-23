from ThreadedTCPServer import ThreadedTCPServer
from FaceCropTCPHandler import FaceCropTCPHandler
import socket


def _read_ip_from_temp():
	with open('../raspy/ip.city.temp', 'r') as f:
		ip = f.readline()
		port = int(f.readline())
		return ip, port


class NeighborhoodMonitorCenter(ThreadedTCPServer):
	"""NeighborhoodMonitorCenter (Centro de Monitoreo Barrial)"""

	def __init__(self, *args, **kwargs):
		args = args + (FaceCropTCPHandler,)
		ThreadedTCPServer.__init__(self, *args, **kwargs)
		
		HOST, PORT = _read_ip_from_temp()
		
		# Create a socket (SOCK_STREAM means a TCP socket)
		self.socketToCity = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socketToCity.connect((HOST, PORT))	
