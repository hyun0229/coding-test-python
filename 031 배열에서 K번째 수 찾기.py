N = int(input())
K = int(input())

i = 1
j = K
ans = 0

while i<=j:
    mid = int((i+j)/2)
    cnt = 0
    for i in range(1,N+1):
        cnt += min(int(mid/i),N)
    if cnt < K :
        i = mid+1
    else:
        ans = mid
        j = mid-1

print(ans)
