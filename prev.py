class Node():
	def __init__(self,parent,sets,level,select1,select2):
		self.parent = parent
		self.sets = sets
		self.select1 = select1
		self.select2 = select2
		self.level = level
		self.path = None
		self.payoff = None
		self.child_no = len(sets)
		self.childs = []
		self.player = level%2

	def max_payoff(self):
		if self.childs:
			m = max(self.childs, key= lambda x : x.payoff)
			self.path = m
			self.payoff = self.path.payoff


'''sets = list(range(0,4))
#global i
i =0 
level = 0 
parent = None
select1=[]
select2=[]'''

def calcpayoff(l1,l2):
	 #(sum(l1)/len(l1),sum(l2)/len(l2))
	 if len(l1)==0:
	 	sum1 =0
	 else:
	 	sum1=sum(l1)/len(l1)
	 if len(l2)==0:
	 	sum2=0
	 else:
	 	sum2 = sum(l2)/len(l2)
	 return (sum1,sum2)

def tarverse(root):
	if root.child_no==0:
		return (root.payoff,root)
	temp = [tarverse(j) for j in root.childs]
	root.payoff = max(temp)[0]
	root.path=max(temp)[1]


def nasheq():
	return (l[-1].select1,l[-1].select2)


def create(sets,parent,level,select1,select2):
	a = Node(parent,sets,level,select1,select2)
	if parent!=None:
		a.parent.childs.append(a)
	#i += 1
	#print(a.sets)
	#print(a.sets,a.select1,a.select2)
	#print(a.player)
	if a.child_no==0:
		a.payoff = calcpayoff(select1,select2)
		#print(a.sets,a.select1,a.select2)
		l.append(a)
	else:
		parent = a
		#temp=a.selected.copy()
		if a.player==0:
			temp=a.select1.copy()
		else:
			temp=a.select2.copy()
		#print(temp)
		for j in range(a.child_no):
			temp.append(a.sets[j])
			if a.player==0:
				create(a.sets[j+1:],parent,level+1,temp.copy(),a.select2.copy())
			else:
				create(a.sets[j+1:],parent,level+1,a.select1.copy(),temp.copy())
	
	return a
l=[]
#i= 0
#l=[]
#root = create(sets,parent,level,select1,select2	)

#print(root.child_no)

#print(i)
#print(tarverse(root))
