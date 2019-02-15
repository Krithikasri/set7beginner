N=int(input())
if(N%10!=0):
	x=N%10
	N=N+(10-x)
	print(N)
else:
	print(N)
