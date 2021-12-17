from sys import argv
import sys
import math
import time
from libnum import xgcd, invmod, n2s



def readcomponents(vartype):
	if (vartype=="int"):
		n=int(myfile.readline())
		c1=int(myfile.readline())
		c2=int(myfile.readline())
		e1=int(myfile.readline())
		e2=int(myfile.readline())
		print("[+]Components have been correctly read"+"\n")
		return [n,c1,c2,e1,e2]
		
	else:
		n=int(myfile.readline(), 16)
		c1=int(myfile.readline(), 16)
		c2=int(myfile.readline(), 16)
		e1=int(myfile.readline(), 16)
		e2=int(myfile.readline(), 16)
		print("[+]Components have been correctly read"+"\n")
		return [n,c1,c2,e1,e2]

'''
Generate the parameter s1 and s2.
It tries different combinations inverting the exponents and sometimes also the ciphertexts
'''
def genparameters(e1, e2):
	s1=0
	s2=0
	if math.gcd(e1, e2)==1:
		s1, s2, gcdn = xgcd(e1, e2)
		print("[+]s1: "+str(s1)+"\n[+]s2: "+str(s2)+"\n")	
		return s1,s2			
	else:
		sys.exit("[-]The two exponents "+str(e1)+" and "+str(e2)+" are not coprimes. Quitting"+"\n")
		
'''
Decrypting phase, it is the only moment in which some interaction with the user could be necessary.
If it seems stuck, pressing CTRL+C it catches the exception and tries a different combination of 
ciphertexts, finding new parameters s1 and s2 and trying again to decrypt. 
If it does not work, the decryption fails.
'''
def decrypt(s1, s2):
	mint=0

	print("[=]Decrypting: if the operation takes too much time(>1 minute), press Ctrl+C to try another combination\n")

	
	try: 
		if s1<0:
			
			cinv=pow(components[1], -1, components[0]) #modular inverse
			mint=int(((components[2]**s2)*(cinv**(-s1)))%components[0])
			
		else:
			if s2<0:

				cinv=pow(components[2], -1, components[0]) #modular inverse
				mint=int(((components[1]**s1)*(cinv**(-s2)))%components[0])

		decode(mint)		
		
		
	except:
		try:
			
			print("[-]Trying another combination"+"\n")
			if s2 < 0:
				components[2] = invmod(components[2], components[0])
				s2 = -s2
				
			if s1 < 0:
				components[1] = invmod(components[1], components[0])
				s1 = -s1
				
			mint=(pow(components[1],s1,components[0]) * pow(components[2],s2,components[0])) % components[0]
			decode (mint)
			
		except:
			sys.exit("[-]Decryption Failed. Quitting.")

		
#it takes the integer message and decrypts it showing the result and the time elapsed			
def decode(mint):
		mhex=hex(mint)[2:]


		by=bytes.fromhex(mhex)
		m=by.decode("ASCII")
		print("[+]The integer decrypted message is:\n"+str(mint)+"\n")
		print("[+]The hexadecimal decrypted message is:\n"+mhex+"\n")
		print("[+]The decrypted message is:\n\t"+m+"\n")	
		end=time.time()
		elapsed = time.strftime("%M:%S", time.gmtime(end - start))
		print("Time elapsed: "+ str(elapsed))	
		

#check if the arguments are correct
if len(argv)!=3:
	print("Usage:\n\tpython3 RSAcma.py <int/hex> <filename>\n")
	print("The file should contain on each line:\nModulus\nFirst Ciphertext\nSecond Ciphertext\nFirst Exponent\nSecond Exponent\n")
	sys.exit()
script, vartype, filename = argv
try:
	myfile=open(filename, "r")
except:
	sys.exit("[-]Could not open the file "+filename+". Check that it exists or that is not corrupted")
	
components=readcomponents(vartype) #read modulus exponents and ciphertext

myfile.close()

start=time.time()

s1, s2= genparameters(components[3], components[4])

decrypt(s1, s2)

