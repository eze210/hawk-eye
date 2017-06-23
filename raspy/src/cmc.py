import socket, fcntl, struct
from CityMonitorCenter import CityMonitorCenter


def _get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


if __name__ == "__main__":
    HOST, PORT = _get_ip_address('eth0'), 9990
    #HOST, PORT = 'localhost', 9990

    with open('./ip.city.temp', 'w') as f:
        f.write('%s%c%d' % (HOST, '\n', PORT))

    # Create the server, binding to localhost on port 9990
    server = CityMonitorCenter((HOST, PORT))

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
