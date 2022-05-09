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
'''
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
