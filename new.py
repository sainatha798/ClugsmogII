import numpy as np

def dist(a,b):
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
		self.dist_datapt_datapt = {}
		self.dissimilarity = {}
		self.near_neigh ={}
		self.clusters={}
		self.centers=[]#list of centers
		self.cent_to_cluster={}#
		#self.initialise()
	def dist(self,a,b):
		return np.linalg.norm(np.array(a)-np.array(b))
	
	def initialise(self):
		for idx,datapt in enumerate(self.data):
			self.idx_to_datapt[idx]=datapt
			self.datapt_to_idx[tuple(datapt)]=idx

		self.dist_datapt_datapt = {i:{j:self.dist(self.idx_to_datapt[i],self.idx_to_datapt[j]) for j in range(self.no_of_pts)} for i in range(self.no_of_pts)}
		#del d(a,a)
		for i in self.dist_datapt_datapt:
			del self.dist_datapt_datapt[i][i]

		max_dist =  max(max([[z for z in v.values()] for v in self.dist_datapt_datapt.values()]))

		self.disimmilarity = {i:sum(self.dist_datapt_datapt[i].values())/self.no_of_pts for i in range(self.no_of_pts)}

		for i in self.dist_datapt_datapt:
			p = list(self.dist_datapt_datapt[i].items())
			p.sort(key=lambda x : x[1])
			self.near_neigh[i] = [key for (key,value) in p][:self.L]
			self.labels = np.zeros(self.no_of_pts)
			count = 0

			'''every cluster is first identfied by a key the cluster no which inturn is a dict containing 'center' and 'pts' '''
		#intialisint the K clusters

		obj = set(list(range(self.no_of_pts)))
		dis = self.disimmilarity.copy()
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

		print(self.labels)
		print(self.clusters)
