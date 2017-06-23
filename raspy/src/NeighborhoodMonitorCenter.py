from ThreadedTCPServer import ThreadedTCPServer
from FaceCropTCPHandler import FaceCropTCPHandler


class NeighborhoodMonitorCenter(ThreadedTCPServer):
    """NeighborhoodMonitorCenter (Centro de Monitoreo Barrial)"""

    def __init__(self, *args, **kwargs):
        args = args + (FaceCropTCPHandler,)
        ThreadedTCPServer.__init__(self, *args, **kwargs)
