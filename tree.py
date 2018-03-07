class Node():
	def __init__(self,parent,set,level,selected):
		self.parent = parent
		self.set = set
		self.selected = selected
		self.level = level
		self.path = None
		self.payoff = None
		self.child_no = len(set)
		self.childs = []

	def max_payoff(self):
		if self.childs:
			m = max(self.childs, key= lambda x : x.payoff)
			self.path = m
			self.payoff = self.path.payoff


set = range(0,10)
#global i
i =0 
level = 0 
parent = None
selected =None


def create(set,parent,level,selected):
	a = Node(parent,set,level,selected)
	if parent!=None:
		a.parent.childs.append(a)
	#i += 1
	print(a.child_no)
	if a.child_no==0:
		a.payoff = a.parent.set[0]
	else:
		parent = a
		for j in range(a.child_no):
			create(set[j+1:],parent,level+1,set[:j+1])
	
	return a

i= 0
root = create(set,parent,level,selected)
print(root.child_no)
#print(i)