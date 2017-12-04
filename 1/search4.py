#!/usr/bin/env python3
#Google Maps Geocode using socket

import socket
from urllib.parse import quote_plus

req = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-agent: script.py\r\n\
Connection: close\r\n\
\r\n\
"""

def geocoder(address):
	s = socket.socket()
	s.connect(("maps.google.com", 80))
	r = req.format(quote_plus(address))
	s.sendall(r.encode('ascii'))
	raw_reply = b''
	while True:
		more = s.recv(4096)
		if not more:
			break
		raw_reply += more
	print(raw_reply.decode('utf-8'))
if __name__ == '__main__':
	geocoder("Magnum Opus Apartments")