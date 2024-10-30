import sys
input = sys.stdin.readline

n,m = map(int,input().split())
als = list(map(int,input().split()))
dls = []
c = [0] * m # 각 나머지의 수
temp = 0
for i in als:
    temp +=i
    dls.append(temp)

cnt = 0 

for i in range(n):
    remainder = dls[i] % m
    if remainder== 0 :
        cnt +=1
    c[remainder] +=1

for i in range(m):
    if c[i]>1:
        cnt += c[i]*(c[i]-1) //2 # 정수로 바꾸기 위해 //사용

        
print(cnt)