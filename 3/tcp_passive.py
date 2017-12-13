#!/usr/bin/env python3

import argparse,socket

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("Expected %d bytes but got %d bytes instead" % (length, len(data)))
        data += more
    return data

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    while True:
        sc, sockname = sock.accept()
        print("Got a connection from {}".format(sockname))
        print("Socket name: ", sc.getsockname())
        print("Socket peer: ", sc.getpeername())
        msg = recvall(sc, 7)
        print("Incoming message: ", repr(msg))
        sc.sendall(b"Goodbye")
        sc.close()
        print("Connection closed")

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Got connection name: ", sock.getsockname())
    sock.connect((host, port))
    sock.sendall(b'Hello!!')
    rep = recvall(sock, 7)
    print("Server said: ", repr(rep))
    sock.close()

if __name__ == "__main__":
    choices = {"client": client, "server": server}
    parser = argparse.ArgumentParser(description="Send and Receive TCP")
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)