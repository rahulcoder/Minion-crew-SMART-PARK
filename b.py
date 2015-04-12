#SEND DATA IN ENCODED FORMAT

import mraa
import time

pin = mraa.Gpio(8)
pin.dir(mraa.DIR_OUT)
ctr = 0
f = open("database.txt","r")
pin.write(1)
pin.write(0)

while True:
	msg = f.readline()
	if msg:
		for i in list(msg):
			if i=='1':
				pin.write(1)
				time.sleep(0.5)
			else:
				pin.write(0)
				time.sleep(0.5)
	else:
		break
f.close()
pin.write(0)
 
