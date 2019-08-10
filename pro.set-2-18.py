#a
yii,uii=map(int,input().split())
tem=[]
x=0
for u in range(yii):
    tem.append(list(map(int,input().split())))   
for u in range(yii):
    for j in range(uii-1):
        for k in range(j+1,uii+1):
            if tem[u][j:k]==[1]*len(tem[u][j:k]):
                 if all(tem[p+u][j:k]==[1]*len(tem[p+u][j:k]) for p in range(len(tem[u][j:k])-1)):
                     if len(tem[u][j:k])>x:
                        x=len(tem[u][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for u in range(x):
    print(*[1]*x) 
