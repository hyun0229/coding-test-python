n = int(input())
p_ls = []
ls = []
chk_ls = []
seq = 0
for i in range(n):
    num = int(input())
    ls.append(num)

for i in range(1,n+1):
    chk_ls.append(i)
    p_ls.append("+")
    while chk_ls and chk_ls[-1] == ls[seq]:
        chk_ls.pop()
        p_ls.append("-")
        seq+=1
    

if chk_ls:
    print("NO")

else : 
    for i in p_ls:
        print(i)