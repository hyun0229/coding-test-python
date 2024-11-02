from collections import deque

n = int(input())

card_q = deque()

for i in range(1,n+1):
    card_q.appendleft(i)

flag = True
while len(card_q)>1:
    """if flag:
        card_q.pop()
        flag = False
    else:
        temp = card_q.pop()
        card_q.appendleft(temp)
        flag = True""" # 내 풀이
    card_q.pop()
    card_q.appendleft(temp = card_q.pop()) #책 풀이
print(card_q[0])
        





