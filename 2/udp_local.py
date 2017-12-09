#!/usr/bin/env python3

import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print("Listening at socket {} on port {}".format(sock.getsockname(), port))
    while True:
        data, addr = sock.recvfrom(MAX_BYTES)
        txt = data.decode('ascii')
        print("The client at {} says {!r}".format(addr, txt))
        txt = "Your data was {} bytes long".format(len(data))
        data = txt.encode('ascii')
        sock.sendto(data, addr)

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    txt = "Your time is {}".format(datetime.now())
    data = txt.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print("Me (the client) has an address {}".format(sock.getsockname()))
    data, addr = sock.recvfrom(MAX_BYTES)
    txt = data.decode('ascii')
    print("The server at {} replied: {!r}".format(addr, txt))

if __name__ == "__main__":
    choices = {"client": client, "server": server}
    parser = argparse.ArgumentParser(description="Send and Receive on UDP locally")
    parser.add_argument('role', choices=choices, help="Select one role from client/server")
    parser.add_argument('-p', metavar='PORT', default=1060, type=int, help="UDP port (default: 1060)")
    args = parser.parse_args()
    func = choices[args.role]
    func(args.p)