#!/usr/bin/python

var1=raw_input("Please enter a list: ")
var2=raw_input("Please enter a list: ")

var1 = var1.strip('[')
var1 = var1.strip(']')

var2 = var2.strip('[')
var2 = var2.strip(']')

list1 = var1.split(',')
list2 = var2.split(',')

for i in range(0,len(list1)):
	list1[i]=int(list1[i].strip())

for i in range(0,len(list2)):
	list2[i] = int(list2[i].strip())

itersection=[]
union=[]
for i in range(0,len(list1)):
	if(list1[i] not in union):
		union.append(list1[i])

for i in range(0,len(list2)):
	if(list2[i] not in union):
		union.append(list2[i])

for i in range(0,len(list1)):
	for j in range(0,len(list2)):
		if(list1[i]==list2[j]):
			itersection.append(list1[i])

union.sort()
itersection.sort()
print(union)
print(itersection)

