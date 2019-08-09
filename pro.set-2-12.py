#a
r,n=map(int,input().split())
nk=list(map(int,input().split()))
l1=[]
for j in range(0,n):
     z,y=map(int,input().split())
     l1.append([z,y])
for j in range(m):
     lower=l1[j][0]
     upper=l1[j][1]
     u=sum(nk[lower-1:upper])
     print(u)
