#STORES DATA ON THE CHIP

f = open("database.txt","w")

codes = {"A":"1000001","B":"1000010","C":"1000011"}

msg = raw_input("ENTER HSRP NUMBER : ")
for i in list(msg):
	f.write(codes[i] + "\n")
f.write("1111111")
f.close()
