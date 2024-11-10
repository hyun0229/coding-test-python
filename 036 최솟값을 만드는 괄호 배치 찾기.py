import sys
input = sys.stdin.readline
ls = list(map(str,input().split('-')))

def sumP(n):
    sum = 0
    tmp = str(n).split("+")
    for i in tmp:
        sum+= int(i)
    return sum

ans = sumP(ls[0])
for i in range(1,len(ls)):
    ans-= sumP(ls[i])

print(ans)