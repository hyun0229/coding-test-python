import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
ls_mirro = [[0]*(m+2) for i in range(n+2)]
goto = [(-1,0),(1,0),(0,-1),(0,1)]
a=0
for i in range(1,n+1):
    x = input()
    for j in range(1,m+1):
        ls_mirro[i][j] = int(x[j-1])

def mirro_BFS(start_x,start_y):
    q_mirro = deque()
    q_mirro.append((start_x,start_y))
    
    while q_mirro:
        now_nd = q_mirro.pop()
        x = now_nd[0]
        y = now_nd[1]
        for i,j in goto:

            if(ls_mirro[x+i][y+j] == 1 and not (start_x == x+i and start_y == y+j)):
                q_mirro.appendleft((x+i,y+j))
                ls_mirro[x+i][y+j] = ls_mirro[x][y]+1

mirro_BFS(1,1)
print(ls_mirro[n][m])


"""
for i in ls_mirro:
    for j in i:
        print(j,end=" ")
    print()

"""