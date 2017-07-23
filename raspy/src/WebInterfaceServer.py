from ThreadedTCPServer import ThreadedTCPServer
from WebInterfaceTCPHandler import WebInterfaceTCPHandler


class WebInterfaceServer(ThreadedTCPServer):
    """WebInterfaceServer"""

    def __init__(self, *args, **kwargs):
        args = args + (WebInterfaceTCPHandler,)
        ThreadedTCPServer.__init__(self, *args, **kwargs)
