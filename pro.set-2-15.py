#a
venk=input()
res=map(int,input().split())
bin=[]
for o in res:
    eat=bin(o)
    bin.append(eat)
fine=sorted(bin)
fine.reverse()
for u in fine:
    print(int(u,2))
