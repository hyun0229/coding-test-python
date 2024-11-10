from queue import PriorityQueue

n = int(input())
p = PriorityQueue()
m = PriorityQueue()
ans = 0
for i in range(n):
    num = int(input())
    if num > 1:
        p.put(-1*num)
    elif num ==1:
        ans+=num
    else:
        m.put(num)
while p.qsize()>1:
    x = p.get()
    y = p.get()
    ans += x*y

while m.qsize()>1:
    x = m.get()
    y = m.get()
    ans += x*y
    

if not p.empty():
    ans += -1*p.get()
if not m.empty():
    ans += m.get()

print(ans)