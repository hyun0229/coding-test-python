import sys
input = sys.stdin.readline

def check(chk_ls,A,C,G,T):
    return chk_ls[ord('A')-65] >= A and chk_ls[ord('C')-65] >= C and chk_ls[ord('G')-65] >= G and chk_ls[ord('T')-65] >= T
    

chk_ls = [0]*26
s,p = map(int,input().split())

ls = input()
A,C,G,T = map(int,input().split())

for j in range(p):
    chk_ls[ord(ls[j])-65]+=1

cnt = 0
i, j = 0, p
while(j<s):
    if check(chk_ls,A,C,G,T):
        cnt+=1
    chk_ls[ord(ls[i])-65] -= 1
    chk_ls[ord(ls[j])-65] += 1
    i+=1
    j+=1
if check(chk_ls,A,C,G,T):
    cnt+=1

print(cnt)