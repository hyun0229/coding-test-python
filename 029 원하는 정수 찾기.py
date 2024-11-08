import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
a_ls = list(map(int,input().split()))
a_ls.sort()
m = int(input())
f_ls = list(map(int,input().split()))

def binary_search(v):
    global n
    i,j = 0, n-1
    result = 0
    while True:
        find = (i+j)//2
        if a_ls[find] == v:
            result = 1
            break
        elif i>=j:
            break
        else:
            if a_ls[find] > v:
                j = find
            else:
                i = find+1
    return result

for i in f_ls:
    print(str(binary_search(i))+"\n")
