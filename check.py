from numpied import *

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
		print(ir_c/(ia_c+ir_c))
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
			pts = self.clusters[key]['pts']
			for i in self.clusters[key]['pts']:
				conn+= len(pts&set(self.near_neigh[i].tolist()))/self.L
			conn /= len(self.clusters[key]['pts'])
		print(conn)
		return conn
