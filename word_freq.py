#!/usr/bin/python

import sys
import operator

dic={}
list1=[]
fname = sys.argv[1]
num = int( sys.argv[2])

with open (fname,"r") as f:
	lines = f.readlines()
	for ln in lines:
		list1=ln.split()
		for i in range(0,len(list1)):
			if list1[i] in dic:
				dic[list1[i]]=dic.get(list1[i])+1
			else:
				dic[list1[i]]=1


final=sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
for i in range(0,num):
	word=final[i][0].ljust(10)
	freq=str(final[i][1]).rjust(10)
	output=word+freq
	print(output)
	
		
