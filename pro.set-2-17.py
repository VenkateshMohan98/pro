t, g = map(int, input().split())
y = list(map(int, input().split()))
for j in permutations(y, 2):
    if sum(j) == g:
        print('yes')
        break
else:
    print('no')
