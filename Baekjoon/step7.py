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

# 1193
x = int(input())

line = 0
max = 0
while x > max:
    line += 1
    max += line

gap = max - x

if line % 2 == 0:
    num = line - gap
    den = gap + 1
else:
    num = gap + 1
    den = line - gap

print("%s/%s" % (num, den))
