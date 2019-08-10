count1=int(input())
array=[]
vv=[]
for j in range(count1):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        vv.append(num)
vv.sort()
for j in vv:
    print(j,end=' ')
    #a
