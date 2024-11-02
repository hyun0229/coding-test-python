import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
visited = [0]*(n+1)
flag = False 
def DFS(num,lv):
    global flag
    if lv == 5:
        print("1")
        flag = True
        return
    else:
        visited[num] +=1
        for i in A[num]:
            if not flag and visited[i]== 0:
                DFS(i,lv+1)
        visited[num] -=1

for i in range(m):
    x,y = map(int,input().split())
    A[x].append(y)
    A[y].append(x)

for i in range(n):
    if flag:
        break
    DFS(i,1)
    
if not flag:
    print("0")
