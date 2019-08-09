    import math
r3,k3=map(int,input().split())
sp1=[]
bb1=list(map(int,input().split()))
for j in range(0,k3):
    l1,h1=map(int,input().split())
    sp1.append([l1,h1])
for j in sp1:
    ss1=j[0]-1
    oo1=j[1]-1
    print(math.gcd(bb1[ss1],bb1[oo1]))
