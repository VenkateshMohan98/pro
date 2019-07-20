from itertools import combinations
N,K=map(int,input().split())
LIS=len(str(N))
LIS1=list(combinations(str(N),LIS-K))
LIS1=sorted(LIS1)
print("".join(LIS1[0]))
