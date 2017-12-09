#!/usr/bin/env python3

import argparse, socket, random
from datetime import datetime

MAX_BYTES = 65535

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print("Listening at socket {} on port {}".format(sock.getsockname(), port))
    while True:
        data, addr = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print("Packet from {} dropped".format(addr))
            continue
        txt = data.decode('ascii')
        print("The client at {} says {!r}".format(addr, txt))
        txt = "Your data was {} bytes long".format(len(data))
        data = txt.encode('ascii')
        sock.sendto(data, addr)

def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((hostname, port))
    txt = "Your time is {}".format(datetime.now())
    data = txt.encode('ascii')
    delay = 0.1 #secs
    print("Me (the client) has an address {}".format(sock.getsockname()))
    while True:
        sock.send(data)
        sock.settimeout(delay)
        print("Will wait for {} secs for reply".format(delay))
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout:
            delay *= 2 #exponential backoff
            if delay > 2.0:
                raise RuntimeError("Server appears to be down")
        else:
            break
    #data, addr = sock.recvfrom(MAX_BYTES)
    txt = data.decode('ascii')
    print("The server at {} replied: {!r}".format(hostname, txt))

if __name__ == "__main__":
    choices = {"client": client, "server": server}
    parser = argparse.ArgumentParser(description="Send and Receive on UDP")
    parser.add_argument('role', choices=choices, help="Select one role from client/server")
    parser.add_argument('host', help="Server: Interface to listen at; Client: Host to connect to")
    parser.add_argument('-p', metavar='PORT', default=1060, type=int, help="UDP port (default: 1060)")
    args = parser.parse_args()
    func = choices[args.role]
    func(args.host, args.p)