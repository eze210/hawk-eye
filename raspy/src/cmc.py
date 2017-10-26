import socket, fcntl, struct,  threading
from CityMonitorCenter import CityMonitorCenter
from WebInterfaceServer import WebInterfaceServer
import Apiserver
import sys


def _parse_parameters(args):
    if len(args) == 4:
        return args[1], int(args[2]), int(args[3])
    else:
        raise RuntimeError("Invalid parameters")
    

if __name__ == "__main__":
    HOST, PORT, PORT_WEB = _parse_parameters(sys.argv)

    # Create the server, binding to host on specified port or 9990
    faceRecognizerServer = CityMonitorCenter((HOST, PORT))

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    serverThread = threading.Thread(target=faceRecognizerServer.serve_forever)
    # Exit the server thread when the main thread terminates
    serverThread.daemon = True
    serverThread.start()

    # Create the WebAPI server, binding to host on specified port or 9991
    # and activate it; this will keep running until you
    # interrupt the program with Ctrl-C
    Apiserver.app.run(host=HOST, port=PORT_WEB)

    faceRecognizerServer.shutdown()
    faceRecognizerServer.server_close()
