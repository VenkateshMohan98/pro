#a
b1=int(input())
o=list(map(int,input().split()))
x=[1]*b1
for j in range(b1):
    if j==0:
        if o[j]>o[j+1]:
            x[j]=x[j]+x[j+1]
    elif j>0:
        if o[j]>o[j-1]:
            x[j]=x[j]+x[j-1]
print(sum(x))
