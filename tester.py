from numpied import *
from check import *

f = open('data','r')
l=[]
for i in f.readlines():
	l.append(list(map(float,i.split(' '))))
#print(l[:6])
#a=Cluster(l,6,20,0.007)
#a.initialise()
b=Test(l,6,20,0.007)
b.initialise()
b.Rsquare()
b.Conn()
b.step2()
#print(b.gravity)