from sys import argv
import sys
import math
import time

inverted=False

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
def genparameters(e1, e2, inverted):
	s1=0
	s2=0
	if math.gcd(e1, e2)==1:
		while (True):
			s2=((e1*s1-1)/e2)
			if(s2.is_integer()):
				s2=int(-s2)
				if (math.gcd(components[1], components[0])!=1 and math.gcd(components[2], components[0])!=1):
					sys.exit("[-]None of the ciphertexts are coprime with the modulus. Quitting\n")


				i=1
				if inverted:
					i=2
				if (math.gcd(components[i], components[0])!=1):
				

					print("[=]Trying another combination\n")
					inverted=True
					s1,s2, inverted=genparameters(e2,e1, inverted)

					return s1,s2, inverted
				print("[+]Parameter s1: "+str(s1)+"\n[+]Parameter s2: "+str(s2)+"\n")
				return s1, s2, inverted
				break
			else:
				s1-=1
	else:
		sys.exit("[-]The two exponents "+str(e1)+" and "+str(e2)+" are not coprimes. Quitting"+"\n")
		
'''
Decrypting phase, it is the only moment in which some interaction with the user could be necessary.
If it seems stuck, pressing CTRL+C it catches the exception and tries a different combination of 
ciphertexts, finding new parameters s1 and s2 and trying again to decrypt. 
If it does not work, the decryption fails.
'''
def decrypt(s1, s2, inverted):
	mint=0
	i=1
	j=2
	if inverted:
		i=2
		j=1
		print("[=]Ciphertexts inverted\n")

	print("[=]Decrypting: if the operation takes too much time(>1 minute), press Ctrl+C to try another combination\n")

	try:
		try: 

			cinv=pow(components[i], -1, components[0]) #modular inverse
			mint=int(((components[j]**s2)*(cinv**(-s1)))%components[0])

		except:
			print("[-]The parameter s1 and s2 have to be inverted"+"\n")
			s1=-s1
			s2=-s2
			print("[+]Parameter s1: "+str(s1)+"\n[+]Parameter s2: "+str(s2)+"\n")
			print("[=]Decrypting: if the operation takes too much time (>1 minute), press Ctrl+C to try another combination\n")


			cinv=pow(components[i], -1, components[0]) #modular inverse
			mint=int(((components[j]**s1)*(cinv**(-s2)))%components[0])


		
		mhex=hex(mint)[2:]
		
		try:
			by=bytes.fromhex(mhex)
			m=by.decode("ASCII")
			print("[+]The integer decrypted message is:\n"+str(mint)+"\n")
			print("[+]The hexadecimal decrypted message is:\n"+mhex+"\n")
			print("[+]The decrypted message is:\n\t"+m+"\n")
			end=time.time()
			elapsed = time.strftime("%M:%S", time.gmtime(end - start))
			print("Time elapsed: "+ str(elapsed))

		except Exception as e:
			print("[-]The file could not be converted to ASCII\n"+str(e)+"\n")
			print("[=]Trying another combination\n")
			if inverted:
				sys.exit("[-]Decryption Failed. Quitting.\n")
				
			inverted=True
			decrypt(s1, s2, inverted)
	except:
		if inverted:
			sys.exit("[-]Decryption Failed. Quitting.\n")
			
		invert=True
		s1,s2, inverted=genparameters(components[4],components[3], inverted)
		decrypt(s1,s2,inverted)

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

s1, s2, inverted= genparameters(components[3], components[4], inverted) 

decrypt(s1, s2, inverted)

