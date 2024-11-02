import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int,input().split())
A = [[] for _ in range(n + 1)]
visited = [0]+[0]*n

def DFS(num):
    visited[num] +=1
    for i in A[num]:
        if visited[i]== 0:
            DFS(i)

for i in range(m):
    x,y = map(int,input().split())
    A[x].append(y)
    A[y].append(x)

cnt = 0
for i in range(1,n+1):
    if visited[i]==0:
        cnt +=1
        DFS(i)
print(cnt)