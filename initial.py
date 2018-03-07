import numpy as np


#data is a list corresponding to datapoints
def dist(a,b):
	#a,b are two lists , return the distance btw them
	return np.linalg.norm(np.array(a)-np.array(b))

#this maps indices to datapts
data = [[1,0],[0,1],[4,5],[5,6],[6,7],[5,3]]#later this has to be read from files
no_of_pts = len(data)
L = 6
K = 3
beta = 0.4
idx_to_datapt={}
#this maps datapts to indices
datapt_to_idx={}
#populating the above dicts
for idx,datapt in enumerate(data):
	idx_to_datapt[idx]=datapt
	datapt_to_idx[tuple(datapt)]=idx

#calculate distance between all datapts stored as a dict of indices , indices
dist_datapt_datapt = {i:{j:dist(idx_to_datapt[i],idx_to_datapt[j]) for j in range(no_of_pts)} for i in range(no_of_pts)}
#del d(a,a)
for i in dist_datapt_datapt:
	del dist_datapt_datapt[i][i]
#print the distances
print(dist_datapt_datapt)
#calculate disimmilarity of Oi
max_dist =  max(max([[z for z in v.values()] for v in dist_datapt_datapt.values()]))
disimmilarity = {i:sum(dist_datapt_datapt[i].values())/no_of_pts for i in range(no_of_pts)}
#print disimmilarity
#print(disimmilarity)
print(max_dist)
#finding the L nearest neighbours for each datapt in ascending order
near_neigh ={}
for i in dist_datapt_datapt:
	p = list(dist_datapt_datapt[i].items())
	p.sort(key=lambda x : x[1])
	near_neigh[i] = [key for (key,value) in p][:L]
	#print(p)
	#print(near_neigh[i])
labels = np.zeros(no_of_pts)#labels store the cluster no corresponding to each datapt not the $center$
count = 0
clusters={}
centers=[]#list of centers
cent_to_cluster={}#
'''every cluster is first identfied by a key the cluster no which inturn is a dict containing 'center' and 'pts' '''
#intialisint the K clusters
obj = set(list(range(no_of_pts)))
dis = disimmilarity.copy()
while count<K:
	count+=1
	ch,ho = min(dis.items(), key=lambda x :x[1])
	obj -= {ch}
	clusters[count]={}
	
	clusters[count]['center']=ch
	centers.append(ch)
	cent_to_cluster[ch]=count
	clusters[count]['pts']=[ x for x in obj if dist_datapt_datapt[ch][x]/max_dist <= beta]
	#find all pts satisfying dist criteria
	obj -= set(clusters[count]['pts'])
	clusters[count]['pts'].append(ch)
	for x in clusters[count]['pts']:
		labels[x]=count
		del dis[x]
	if not obj:
		break
if obj:
	cen_temp,dist = min([(x ,dist_datapt_datapt[obj][x]) for x in centers],key=lambda y:y[1])
	labels[obj]=cent_to_cluster[cen_temp]
	clusters[labels[obj]]['pts'].append(obj)

print(labels)
print(clusters)