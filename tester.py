from new import *


f = open('data','r')
l=[]
for i in f.readlines():
	l.append(list(map(float,i.split(' '))))
#print(l[:6])
a=Cluster(l[:1500],6,20,0.007)
a.initialise()