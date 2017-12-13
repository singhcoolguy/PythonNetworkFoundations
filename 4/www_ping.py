#!/usr/bin/env python3

#Demonstrates the use of getaddrinfo

import sys, socket, argparse

def connect_to(hostname_or_ip):
    try:
        infolist = socket.getaddrinfo(hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
                                      socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME)
    except socket.gaierror as e:
        print("Name service failure: ", e.args[1])
        sys.exit(1)
    info = infolist[0]
    sock_args = info[0:3]
    addr = info[4]

    sock = socket.socket(*sock_args)

    try:
        sock.connect(addr)
    except socket.error as e:
        print("Network Failure caught: ", e.args[1])
    else:
        print("Successfully connected to ", info[3], "on port 80")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Try to connect to a service on port 80")
    parser.add_argument('host', help="Host name/IP to try to connect to")
    connect_to(parser.parse_args().host)