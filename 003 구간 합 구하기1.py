import sys
input = sys.stdin.readline

"""
내 코드
n,m = map(int,input().split())
ls = list(map(int,input().split()))
sum_ls = []
sum_ls.append(ls[0])
for i in range(1,len(ls)):
    sum_ls.append(ls[i] + sum_ls[i-1])

for a in range(m):
    i,j = map(int,input().split())
    if(i == 1):
        print(sum_ls[j-1])
    else:
        print(sum_ls[j-1]-sum_ls[i-2])
"""

suNo, quizNo = map(int,input().split())
numbers = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int,input().split())
    print(prefix_sum[e]-prefix_sum[s-1])
