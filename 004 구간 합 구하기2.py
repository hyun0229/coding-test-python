import sys
input = sys.stdin.readline

n,q = map(int,input().split())

a_ls = [[0]*(n+1)]
d_ls = [[0]*(n+1) for i in range(n+1)]

for i in range(n):
    row = [0]+list(map(int,input().split()))
    a_ls.append(row)

for i in range(1,n+1):
    for j in range(1,n+1):
        d_ls[i][j] = d_ls[i-1][j] + d_ls[i][j-1] - d_ls[i-1][j-1] + a_ls[i][j]

for i in range(q):
    x1,y1,x2,y2 = map(int,input().split())
    result = d_ls[x2][y2] - d_ls[x1-1][y2] - d_ls[x2][y1-1] + d_ls[x1-1][y1-1]
    print(result)
