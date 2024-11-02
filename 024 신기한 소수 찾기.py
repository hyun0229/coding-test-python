s_ls = [2,3,5,7]
c_ls = [1,3,5,7,9]



def isPrime(num):
    for i in range(2,int(num/2+1)):
        if num%i==0:
            return False
    return True

n = int(input())

def DSF(sosu):
    if len(str(sosu)) == n:
        print(sosu)
    else:
        for i in c_ls:
            if isPrime(sosu*10+i):
                DSF(sosu*10+i)

for i in s_ls:
    DSF(i)