import sys, socket, fcntl, struct,  threading
from NeighborhoodMonitorCenter import NeighborhoodMonitorCenter
import Apiserver


def _parse_parameters(args):
    if len(args) == 6:
        return args[1], int(args[2]), int(args[3]), args[4], int(args[5])
    else:
        raise RuntimeError("Invalid parameters")


if __name__ == "__main__":
    HOST, PORT, PORT_WEB, CITY_HOST, CITY_PORT = _parse_parameters(sys.argv)

    # Create the server, binding to localhost on port 9999
    cmbServer = NeighborhoodMonitorCenter(((HOST, PORT), (CITY_HOST, CITY_PORT)))

    serverThread = threading.Thread(target=cmbServer.serve_forever)
    # Exit the server thread when the main thread terminates
    serverThread.daemon = True
    serverThread.start()

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    Apiserver.app.run(host=HOST, port=PORT_WEB)

    cmbServer.shutdown()
    cmbServer.server_close()
