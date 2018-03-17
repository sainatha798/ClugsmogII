def fn(x,n):

	def p(a,n):
		if n==1:
			return a;
		return a*p(a,n-1)
	for j in x:
		l=p(j,n)
		print(l)
		#print('\n')


x=[1,2,3,4]
n=4
fn(x,n)
