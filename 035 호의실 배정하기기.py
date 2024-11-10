n = int(input())
ls = [[0] *2 for i in range(n)]

for i in range(n):
    x,y = map(int,input().split())
    ls[i][0] = y
    ls[i][1] = x
ls.sort()

ans = 0
chk = 0
for i in range(n):
    if ls[i][0] >= chk:
        chk = ls[i][1]
        ans+=1

print(ans)