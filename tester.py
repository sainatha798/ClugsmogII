from numpied import *
from check import *
import matplotlib.pyplot as plt
f = open('data_3','r')
l=[]
for i in f.readlines():
	l.append(list(map(float,i.split('    '))))
#print(l[:6])
#a=Cluster(l,6,20,0.007)
#a.initialise()
x= [p[0] for p in l]
y=[p[1] for p in l]
plt.scatter(x,y)
plt.show()
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
print(b.centers)
x=[b.idx_to_datapt[i][0] for i in b.centers ]
y=[b.idx_to_datapt[i][1] for i in b.centers]
plt.scatter(x,y)
plt.show()
#print(b.gravity)
