x,t=input().split()
char=abs(len(t)-len(x))
for j in range(len(x)):
  if(len(t)==1 and t[j] in x):
    break
  if(x[j]!=t[j]):
    char=char+1
print(char)
