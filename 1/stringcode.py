#!/usr/bin/env python3

if __name__ == '__main__':
	ib = "\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00"
	ic = ib.decode('utf-16')
	print(repr(ic))

	oc = "We hear you, bro.\n"
	ob = oc.encode('utf-8')
	with open('eagle.txt', 'wb') as f:
		f.write(ob)