#!/usr/bin/env python3

import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocoder(address):
	path = '{}?address={}&sensors=false'.format(base, quote_plus(address))
	connection = http.client.HTTPConnection('maps.google.com')
	connection.request('GET', path)
	rawreply = connection.getresponse().read()
	reply = json.loads(rawreply.decode('UTF-8'))
	print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
	geocoder('Magnum Opus Apartments')