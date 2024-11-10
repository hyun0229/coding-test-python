from queue import PriorityQueue

n = int(input())
q = PriorityQueue()

for i in range(n):
    q.put(int(input()))

ans = 0
while q.qsize()>1:
    x = q.get()
    y = q.get()
    temp = x+y
    ans += temp
    q.put(temp)


print(ans)