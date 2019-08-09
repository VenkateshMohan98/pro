#a
venka,imah=map(int,input().split())
list1=list(map(int,input().split()))
venka=[]
list1.insert(0,0)
for x in range(imah):
     vin=[]
     s=0
     aa,yy=map(int,input().split())
     for j in range(aa,yy+1):         
         s^=list1[j]     
     venka.append(s)
for x in venka:
     print(x)
