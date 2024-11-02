from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
abs_q = PriorityQueue()

for i in range(n):
    x = int(input())
    if x==0:
        if abs_q.empty():
            print("0\n")
        else:
            
            temp = abs_q.get()
            print(str(temp[1])+"\n")
    else:
        abs_q.put((abs(x),x))


