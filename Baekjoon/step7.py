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

def honeycomb(num):
    if num == 1:
        print(1):
    else:
        a = 1
        
