"""
내가 푼 풀이
n = int(input())
score = list(map(int,input().split()))
maxScore = max(score)
sum = 0

for i in score:
    sum += i/maxScore*100

print(sum/n)
"""
#책 풀이
n = input()
mylist = list(map(int,input().split()))
mymax = max(mylist)
sum = sum(mylist)
print(sum*100/mymax/int(n))

#(A / M * 100 + B / M * 100 + C / M * 100) / 3 = (A + B + C)* 100 / M /3