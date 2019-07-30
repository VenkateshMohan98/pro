d1,d2=map(str,input().split())
vmp=0
if len(d1)>len(d2):
  d1,d2=d2,d1
r=0
while r<len(d1):
  vmp+=(ord(d2[r])-ord(d1[r]))
  r+=1
for r in range(r,len(d2)):
  vmp+=ord(d2[r])-ord('a')+1
print(vmp)
