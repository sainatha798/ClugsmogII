import numpy as np
from math import inf

def dista(a,b):
	#a,b are two lists , return the distance btw them
	return np.linalg.norm(np.array(a)-np.array(b))

class Cluster:

	def __init__(self,data,l,k,beta):
		self.data = data
		self.no_of_pts = len(self.data)
		self.L =l
		self.K = k
		self.beta = beta
		self.idx_to_datapt={}
		#this maps datapts to indices
		self.datapt_to_idx={}
		self.dist_datapt_datapt = None
		self.dissimilarity = {}
		self.near_neigh = None
		self.clusters={}
		self.centers=[]#list of centers
		self.cent_to_cluster={}#
		#self.initialise()
	#def dist(self,a,b):
	#	return np.linalg.norm(np.array(a)-np.array(b))
	
	def initialise(self):
		self.data = np.array(self.data)
		self.gravity = np.sum(self.data,axis=0)/self.data.shape[0]
		for idx,datapt in enumerate(self.data):
			self.idx_to_datapt[idx]=datapt
			self.datapt_to_idx[tuple(datapt)]=idx

		#self.dist_datapt_datapt = {i:{j:dista(self.idx_to_datapt[i],self.idx_to_datapt[j]) for j in range(self.no_of_pts)} for i in range(self.no_of_pts)}
		self.dist_datapt_datapt = np.linalg.norm(self.data - self.data[:,None], axis=-1)
		self.disimmilarity = np.sum(self.dist_datapt_datapt,axis=1)/self.no_of_pts
		self.dist_datapt_datapt[np.arange(self.dist_datapt_datapt.shape[0]), np.arange(self.dist_datapt_datapt.shape[0])] = np.nan
		#del d(a,a)
		#for i in self.dist_datapt_datapt:
		#	del self.dist_datapt_datapt[i][i]

		max_dist =  np.max(self.dist_datapt_datapt)

		print('calc done\n')
		#self.disimmilarity = {i:sum(self.dist_datapt_datapt[i].values())/self.no_of_pts for i in range(self.no_of_pts)}

		'''for i in self.dist_datapt_datapt:
			p = list(self.dist_datapt_datapt[i].items())
			p.sort(key=lambda x : x[1])
			self.near_neigh[i] = [key for (key,value) in p][:self.L]'''
		self.near_neigh = np.argsort(self.dist_datapt_datapt,axis=1)[:,:self.L]
		self.dist_datapt_datapt[np.arange(self.dist_datapt_datapt.shape[0]), np.arange(self.dist_datapt_datapt.shape[0])] = 0
		self.labels = np.zeros(self.no_of_pts)
		count = 0

			#intialisint the K clusters

		obj = set(list(range(self.no_of_pts)))
		dis = {}
		for i in range(self.disimmilarity.shape[0]):
			dis[i]=self.disimmilarity[i]
		while count<self.K:
			count+=1
			ch,ho = min(dis.items(), key=lambda x :x[1])
			obj -= {ch}
			self.clusters[count]={}
	
			self.clusters[count]['center']=ch
			self.centers.append(ch)
			self.cent_to_cluster[ch]=count
			self.clusters[count]['pts']=[ x for x in obj if self.dist_datapt_datapt[ch][x]/max_dist <= self.beta]
			#find all pts satisfying dist criteria
			obj -= set(self.clusters[count]['pts'])
			self.clusters[count]['pts'].append(ch)
			for x in self.clusters[count]['pts']:
				self.labels[x]=count
				del dis[x]
			if not obj:
				break
		if obj:
			for pt in obj:
				cen_temp,dist = min([(x ,self.dist_datapt_datapt[pt][x]) for x in self.centers],key=lambda y:y[1])
				self.labels[pt]=self.cent_to_cluster[cen_temp]
				self.clusters[self.labels[pt]]['pts'].append(pt)

		print(self.centers)	#print(self.clusters)
		self.clus_rep_update()
		print(self.centers)
		print(self.labels)
		#print(len(self.labels))
		#print(self.near_neigh)
	def clus_rep_update(self,key=0):
		if key==0:
			for i in self.clusters:
				temp = self.clusters[i]['pts'][0]
				min = inf
				for j in self.clusters[i]['pts']:
					val = sum([self.dist_datapt_datapt[j][z] for z in self.clusters[i]['pts'] if j!=z])
					if val<min:
						min = val 
						temp = j
				del self.cent_to_cluster[self.clusters[i]['center']]
				self.centers.remove(self.clusters[i]['center'])
				self.centers.append(temp)
				self.cent_to_cluster[temp] = i
				self.clusters[i]['center'] = temp
		else:
			i=key
			temp = self.clusters[i]['pts'][0]
			min = inf
			for j in self.clusters[i]['pts']:
				val = sum([self.dist_datapt_datapt[j][z] for z in self.clusters[i]['pts'] if j!=z])
				if val<min:
					min = val
					temp = j
			del self.cent_to_cluster[self.clusters[i]['center']]
			self.centers.remove(self.clusters[i]['center'])
			self.centers.append(temp)
			self.cent_to_cluster[temp] = i
			self.clusters[i]['center'] = temp
			