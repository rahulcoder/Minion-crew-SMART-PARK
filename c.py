#DECODES DATA AT ENTRY

import mraa
import time
import sys
import os
os.system("clear")
codes = {"1000001":"A","1000010":"B","1000011":"C"}

ain = mraa.Aio(1)
f = open("slots.txt","r")
msg = ""
ctr = 0
flag = 0
dec = []

while True:
	a = ain.read()
	print a
	if int(a)>800:
		print "INITIATED"
		while True:
			msg = ""
			while ctr<7:
				ctr = ctr + 1
				a = ain.read()
				if int(a)>800:
					msg = msg + "1"
					print "1"
				else:
					msg = msg + "0"
					print "0"
				time.sleep(0.5)
			ctr = 0
			if msg=="1111111" or msg=="0000000":
				flag = 1
				break
			dec.append(msg)
			time.sleep(0.5)
	if flag==1:
		break
msg = ""
for i in dec:
	try:
		msg = msg + codes[i]
	except:
		pass

print "HSRP NUMBER : " + msg
msg = msg + "#"
ind = 0

slots = [0 for i in range(4)]
ctr = 0

while True:
	ind = f.readline()
	try:
		if ind:
			res = int(ind)
			slots[res] = 1
			ctr = ctr + 1
		else:
			break
	except:
		pass
	
f.close()

if ctr==4:
	print "PARKING FULL!!"
	sys.exit()

f2 = open("entry.txt","a")
f = open("slots.txt","a")

for i in range(4):
	if slots[i]==0:
		f2.write(msg + str(i) + "\n")
		f.write(str(i) + "\n")
		print "SLOT NUMBER : " + str(i)
		break

f2.close()
f.close()
	

