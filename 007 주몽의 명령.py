import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

ls = list(map(int,input().split()))
ls.sort()
cnt = 0
i,j = 0,n-1
while i<j:
    if ls[i]+ls[j] < m:
        i+=1
    elif ls[i]+ls[j] > m:
        j-=1
    else :
        cnt +=1
        i+=1
        j-=1

print(cnt)