from ThreadedTCPServer import ThreadedTCPServer
from FaceRecognizeTCPHandler import FaceRecognizeTCPHandler


class CityMonitorCenter(ThreadedTCPServer):
    """CityMonitorCenter (Centro de Monitoreo de la Ciudad)"""

    def __init__(self, *args, **kwargs):
        args = args + (FaceRecognizeTCPHandler,)
        ThreadedTCPServer.__init__(self, *args, **kwargs)
