import sys
input = sys.stdin.readline

def lsnum(x,y,n):
    return (x-1)*n+y-1


n,q = map(int,input().split())
ls = []
prefix_sum = []
temp = 0
for i in range(n):
    ls.extend(map(int, input().split()))

for i in ls:
    temp += i
    prefix_sum.append(temp)


for i in range(q):
    x1,y1,x2,y2 = map(int,input().split())
    if(x1 == 1 and y1 == 1):
        if((x1 == x2 and y1 == y2)):
            print(prefix_sum[lsnum(x1,y2,n)])
        else:
            print(prefix_sum[lsnum(x1,y2,n)]+prefix_sum[lsnum(x2,y2,n)]-prefix_sum[lsnum(x2,y1,n)-1])
    elif(x1 == x2 and y1 == y2):
        print(prefix_sum[lsnum(x1,y2,n)]-prefix_sum[lsnum(x1,y1,n)-1])
    else:
        print(prefix_sum[lsnum(x1,y2,n)]-prefix_sum[lsnum(x1,y1,n)-1]+prefix_sum[lsnum(x2,y2,n)]-prefix_sum[lsnum(x2,y1,n)-1])
