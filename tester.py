from numpied import *
from check import *

f = open('data_3','r')
l=[]
for i in f.readlines():
	l.append(list(map(float,i.split('    '))))
#print(l[:6])
#a=Cluster(l,6,20,0.007)
#a.initialise()
b=Test(l,6,15,0.01)
b.initialise()
print(set(b.labels))
b.Rsquare()
b.Conn()
i=0
while(i<5):
	b.step2()
	print(set(b.labels))
	i+=1
print(len(b.labels))
#print(b.gravity)
