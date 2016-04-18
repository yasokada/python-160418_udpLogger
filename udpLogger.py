import time
import socket
from utilLogger import CUtilLogger

'''
v0.1 2016 Apr. 18
	- import CUtilLogger for logging
'''

def recvData(datsock, rcvdat):
	try:
		data,address = datsock.recvfrom(100)
	except socket.error:
			pass
	else:
		rcvdat = rcvdat + data
		return rcvdat, True
	return rcvdat, False

def procData(rcvdat):
	print rcvdat

def main():
	# incoming data string port
	datip = "" # INADDR_ANY
	datport = 7001
	datsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	datsock.bind((datip, datport))
	datsock.setblocking(0)

	rcvdat = ""

	# receive data
	while 1:
		rcvdat,rcvd = recvData(datsock, rcvdat)
		if rcvd == True and "\n" in rcvdat:
			procData(rcvdat)
			rcvdat = ""

#logger = CUtilLogger()
#logger.add("TEST")
#logger.save()


if __name__ == '__main__':
	main()