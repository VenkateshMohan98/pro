g1=int(input())
p=list(map(int,input().split()))
o=0
for r in range(0,g1-2):
	for s in range(1,g1-1):
		for t in range(2,g1):
			if(p[r]<p[s] and p[s]<p[t]):
				o+=1
print(o)
