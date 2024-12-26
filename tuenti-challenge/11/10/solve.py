from dpkt.pcap import Reader
from dpkt.ethernet import Ethernet
from pyzbar.pyzbar import decode
from PIL import Image

PATH_ICMP = 'icmps.pcap'
PATH_IMAGE = 'out.png'

def main():
	packages = [Ethernet(p).data.data for t, p in Reader(open(PATH_ICMP, 'rb'))]
	print(''.join(chr(p.data.id) for p in packages))
	with open(PATH_IMAGE, 'wb') as fp:
		fp.write(b''.join(p.data.data for p in sorted(packages, key=lambda p: p.data.seq)))
	password = decode(Image.open(PATH_IMAGE).resize((290, 290)))[0].data.decode()
	print(password)
	with open('password.txt', 'w') as fp:
		fp.write(password.split(': ')[1])

if __name__ == '__main__':
	main()