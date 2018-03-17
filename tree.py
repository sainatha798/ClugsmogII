class Node():
	def __init__(self,parent,l_sets,level,l_sels):
		self.parent = parent
		self.sets = l_sets
		self.sels = l_sels
		self.level = level
		self.path = None
		self.payoff = None
		self.child_no = len(self.sets[level%2])
		self.childs = []
		self.player = level%2

	'''def max_payoff(self):
		if self.childs:
			m = max(self.childs, key= lambda x : x.payoff)
			self.path = m
			self.payoff = self.path.payoff'''


sets = [list(range(0,4)),list(range(0,4))]
#global i
i =0 
level = 0 
parent = None
a=[]
b=[]
selected=[a,b]


def create(parent,sets,level,sels):
	a = Node(parent,sets,level,sels)
	print(a.player)
	if parent!=None:
		a.parent.childs.append(a)
	#i += 1
	#print(a.child_no)
	if a.child_no==1:
		a.payoff = a.parent.level
		return a
	else:
		parent = a
		temp_sets = a.sets.copy()
		temp_sels = a.sels.copy()
		for j in range(a.child_no):
			
			temp_sels[a.player].append(temp_sets[a.player][0])
			temp_sets[a.player].pop(0)
			#print(temp_sets,temp_sels)		
			create(parent,temp_sets,level+1,temp_sels)
	
	return a

i= 0
root = create(parent,sets,level,selected)
print(root.child_no)
#print(i)