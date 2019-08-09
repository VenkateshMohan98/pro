#a
f, d = [int(j) for j in input().split()]
g = []
Lis = [int(j) for j in input().split()]
for _ in range(d):
    i, r = [int(j) for j in input().split()]
    g.append(min(Lis[i-1:r]))
for j in g:
    print(j)
