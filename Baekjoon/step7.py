'''
# 1712
import sys
a, b, c = map(int, sys.stdin.readline().split())

breakevenPoint = 0
if b > c or b == c:
    breakevenPoint = -1
else:
    breakevenPoint = a // (c - b) + 1

print(breakevenPoint)

# 2292
n = int(input())

honey = 1
count = 1

if n == 1:
    print(count)
else:
    while n > honey:
        count += 1
        honey += (count * 6)
        
    print(count+1)
'''
# 1193
x = int(input())

sum = 0
row = 0
col = 0
cnt = 0
for i in range(x):
    sum += i
    cnt += 1

    if sum >= x:
        row = cnt - 1
        column = x - (sum - i)
        print("row:", cnt)
        print("column:", column)
        break

num = 0
den = 0

if x == 1:
    print("%s/%s" % (num+1, den+1))
else:
    for j in range(cnt):
        if row % 2 == 0:
            pass

print("%s/%s" % (num, den))
