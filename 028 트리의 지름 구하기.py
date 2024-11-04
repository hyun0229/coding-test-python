from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
nd_ls = [[] for i in range(n+1)]
vistit_nd = [0] * (n+1)
for i in range(1,n+1):
    node = list(map(int,input().split()))
    num = 1
    number = node[0]
    while node[num]!= -1:
        nd_ls[number].append((node[num],node[num+1]))
        num+=2

def tree_BFS(v):
    vistit_nd[v]+=1
    nd_q = deque()
    nd_q.appendleft((v,0))
    max_value = 1
    max_node = 0
    while nd_q:
        n_nd = nd_q.pop()
        if max_value < n_nd[1]:
            max_value = n_nd[1]
            max_node = n_nd[0]
        
        for i in nd_ls[n_nd[0]]:
            if not vistit_nd[i[0]]:
                nd_q.appendleft((i[0],i[1]+n_nd[1]))
                vistit_nd[i[0]] += 1
    return max_value,max_node

result = 0

result,v = tree_BFS(1)
vistit_nd = [0] * (n+1)
result,v = tree_BFS(v)
print(result)
