#!/usr/bin/env python3

import socket, argparse

BUFSIZE = 65535

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print("Listening at {}".format(sock.getsockname()))
    while True:
        data, addr = sock.recvfrom(BUFSIZE)
        txt = data.decode('ascii')
        print("The client at {} says {!r}".format(addr, txt))

def client(network, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    txt = "Broadcast data"
    sock.sendto(txt.encode('ascii'), (network, port))

if __name__ == "__main__":
    choices = {"client": client, "server": server}
    parser = argparse.ArgumentParser(description="Send and Receive on UDP")
    parser.add_argument('role', choices=choices, help="Select one role from client/server")
    parser.add_argument('host', help="Server: Interface to listen at; Client: Host to connect to")
    parser.add_argument('-p', metavar='PORT', default=1060, type=int, help="UDP port (default: 1060)")
    args = parser.parse_args()
    func = choices[args.role]
    func(args.host, args.p)