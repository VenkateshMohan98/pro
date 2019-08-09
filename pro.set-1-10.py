chaa=int(input())
choa=[int(p) for p in input().split(" ")]
chea=0
for r in range(chaa):
      for h in range(r):
           if(choa[h]<choa[r]):
                chea+=choa[h]
print(chea)
