#!/usr/bin/env python3

import argparse, socket, IN

#IN only in Linux

if not hasattr(IN, 'IP_MTU'):
    raise RuntimeError("Can't perform MTU discovery")

def send_big_datagram(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
    sock.connect((host, port))
    try:
        sock.send(b'#' * 65000)
    except socket.error:
        print("Datagram couldn't pass")
        max_mtu = sock.getsockopt(socket.IPPROTO_IP, IN.IP_MTU)
        print("Actual MTU {}".format(max_mtu))
    else:
        print("Datagram sent")

if __name__ == "__main__":
    choices = {"client": client, "server": server}
    parser = argparse.ArgumentParser(description="Send UDP to get MTU")
    parser.add_argument('host', help="Server: Interface to listen at; Client: Host to connect to")
    parser.add_argument('-p', metavar='PORT', default=1060, type=int, help="UDP port (default: 1060)")
    args = parser.parse_args()
    send_big_datagram(args.host, args.p)