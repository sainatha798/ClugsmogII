from numpied import *
from math import ceil
#from tree import *
from prev import *
class Test(Cluster):
	
	def Rsquare(self):
		ir_c=0
		ia_c=0
		for i in self.clusters:
			ir_c += dista(self.clusters[i]['center'],self.gravity)*len(self.clusters[i]['pts'])
			for j in self.clusters[i]['pts']:
				ia_c += self.dist_datapt_datapt[self.clusters[i]['center'],j]
		ir_c=ir_c/self.no_of_pts
		ia_c = ia_c/self.no_of_pts
		#print(ir_c/(ia_c+ir_c))
		return ir_c/(ia_c+ir_c)

	def Conn(self,key=None):
		if key is None:
			conn = 0
			for i in self.clusters:
				pts = set(self.clusters[i]['pts'])
				for j in self.clusters[i]['pts']:
					conn+= len(pts&set(self.near_neigh[j].tolist()))/self.L
			conn=conn/self.no_of_pts


		else:
			conn=0
			pts = set(self.clusters[key]['pts'])
			for i in self.clusters[key]['pts']:
				conn+= len(pts&set(self.near_neigh[i].tolist()))/self.L
			try:
				conn /= len(self.clusters[key]['pts'])
			except:
				conn=0
		#print(conn)
		return conn

	def step2(self):
		self.clu_neigh={}
		self.rev_neigh={}
		#generating conflict clusters
		for i in self.clusters:
			temp=[(j,self.dist_datapt_datapt[self.clusters[j]['center']][self.clusters[i]['center']]) for j in self.clusters if j!=i]
			self.clu_neigh[i]=min(temp,key=lambda x:x[1])
			try:
				self.rev_neigh[self.clu_neigh[i][0]].append((i,self.clu_neigh[i][1]))
			except:
				self.rev_neigh[self.clu_neigh[i][0]]=[(i,self.clu_neigh[i][1])]
		#print(self.clu_neigh)
		self.conflict=[j for j in sorted(self.rev_neigh,key=lambda x:len(self.rev_neigh[x]),reverse=True) if len(self.rev_neigh[j])>1]
		#print(self.conflict)
		#rev_neigh has the corresponding clusters which conflicted for Ci
		for con in self.conflict:
			initial=self.Rsquare()*self.Conn()
			players = [x[0] for x in self.rev_neigh[con]]

			sorted(players,key=lambda x:self.dist_datapt_datapt[self.clusters[x]['center']][self.clusters[con]['center']])
			#print(players)
			i=0
			j=1
			while(j<len(players)):
				if self.Conn(key=players[i])>=self.Conn(key=players[j]):
					leader=players[i]
					follow =players[j]
				else:
					leader=players[j]
					follow=players[i]
				con_pts = set(self.clusters[con]['pts'])
				set_lead = set()
				set_follow = set()
				set_conf = set()
				for ix in self.clusters[leader]['pts']:
					set_lead.update(set(self.near_neigh[ix])&con_pts)
				for ix in self.clusters[follow]['pts']:
					set_follow.update(set(self.near_neigh[ix])&con_pts)
				#print(set_lead,set_follow)
				set_conf.update(set_lead&set_follow)
				set_lead = list(set_lead - set_conf)
				set_follow = list(set_follow - set_conf)
				for ip in range(ceil(0.5*(len(set_lead)))):
					self.clusters[con]['pts'].remove(set_lead[ip])
					self.labels[set_lead[ip]]=leader
					self.clusters[leader]['pts'].append(set_lead[ip])
				for ip in range(ceil(0.5*(len(set_follow)))):
					self.clusters[con]['pts'].remove(set_follow[ip])
					self.labels[set_follow[ip]]=follow
					self.clusters[follow]['pts'].append(set_follow[ip])
				#print(set_conf)
				temp=self.clusters.copy()
				if set_conf:
					#playing game for first 6 elements
					sets = list(set_conf)[:6]
					
					root = create(sets,None,0,[],[])
					#calculating the nash eq
					l=nasheq()[0]
					for ip in l:
						self.clusters[leader]['pts'].append(ip)
						self.clusters[con]['pts'].remove(ip)
						self.labels[ip]=leader
					final=self.Rsquare()*self.Conn()
					if final<initial:
						self.clusters=temp
						for ip in l:
							self.labels[ip]=con
					else:
						print("OK")		
				self.clus_rep_update(leader)
				self.clus_rep_update(follow)
				self.clus_rep_update(con)
					#print(l)				
				i+=1
				j+=1

