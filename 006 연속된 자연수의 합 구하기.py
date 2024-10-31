import sys
input = sys.stdin.readline

n = int(input())

sum = 1
start_index = 1
end_index = 1
cnt = 1 #n 단일만 있을때를 미리 계산


while end_index != n:
    if sum == n :
        cnt += 1
        end_index +=1
        sum  += end_index
    elif sum > n :
        sum -= start_index
        start_index +=1
    else :
        end_index +=1
        sum += end_index

print(cnt) 