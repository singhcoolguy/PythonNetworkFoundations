#!usr/bin/env python3

import socket

def getIP(name):
	addr = socket.gethostbyname(name)
	print("The address of {} is {}".format(name, addr))

if __name__ == '__main__':
	getIP('www.python.org')