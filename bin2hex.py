#!/usr/bin/python

bininput=raw_input()


binlen =len(bininput)

inputcheck=bininput.count('0')+bininput.count('1')
if(inputcheck != len(bininput)):
	print("Invalid input")
	exit(1)
#for i in range(0,binlen):
#	if(bininput[i]!='0' or bininput[i]!='1'):
#		print("Invalid input")
#		exit(1)
if(binlen %16!=0):
	num=binlen//16
	bininput=bininput.zfill(16*(num+1))

binlen =len(bininput)
temp=[]
O=[]
output=''

for i in range(0,binlen,4):
	temp.append(int('0b'+bininput[i:i+4],2))

for i in range(0,binlen//4):
	O.append(format(temp[i],'X'))

for i in range(0,len(O)):
	if(i!=0 and i%4==0):
		output+=' '+O[i]
	else:
		output+=O[i]
print(output)
