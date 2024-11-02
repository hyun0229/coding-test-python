import sys
input = sys.stdin.readline

n = int(input())
nge = [0] * n
ls = list(map(int,input().split()))
chk_ls = []

for i in range(1,n+1):
    while chk_ls and chk_ls[-1] <= ls[-i]:
        chk_ls.pop()
    chk_ls.append(ls[-i])
    if ls[-i] == chk_ls[0]:
        nge[-i] = -1
    else:
        nge[-i] = chk_ls[-2]

for i in nge:
    print(i, end=' ')


