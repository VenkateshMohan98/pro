chatj=int(input())
ph=[]
dog=0
for k in range (0,chatj+1):
    dog=abs((2**k)-chatj)
    ph.append(dog)
kall=min(ph)
print(kall)
