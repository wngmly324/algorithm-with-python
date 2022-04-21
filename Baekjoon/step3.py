'''
# 2739
a = int(input())

for i in range(1,10):
    print("%d * %d = %d" %(a, i, a*i))

# 10950
T = int(input())
res = []

while T:
    a, b = map(int, input().split())
    res.append(a+b)
    T -= 1
    
for i in res:
    print(i)

# 8393
n = int(input())
sum = 0

for i in range(0,n):
    i += 1
    sum += i
    
print(sum)

# 15552
# 빠르게 입력받고 출력하는 문제

# 2741
n = int(input())
for i in range(0,n):
    i += 1
    print(i)

# 2742
n = int(input())
while n:
    print(n)
    n -= 1

# 11021
T = int(input())
res = []

while T:
    a, b = map(int, input().split())
    res.append(a+b)
    T -= 1
    
count = 0

for i in res:
    count += 1
    print("Case #%d: %d" % (count, i))

# 11022
T = int(input())
aList = []
bList = []
res = []

while T:
    a, b = map(int, input().split())
    aList.append(a)
    bList.append(b)
    res.append(a+b)
    T -= 1

count = 0

for i in res:
    count += 1
    print("Case #%d: %d + %d = %d" % (count, aList[count-1], bList[count-1], i))

# 2438
n = int(input())
for i in range(0, n):
    i += 1
    print("*" * i)

# 2439
n = int(input())
i = 0

while n:
    i += 1
    a = " " * (n-1)
    b = "*" * i
    n -= 1
    print(a+b)

# 10871
n, x = map(int, input().split())
a = map(int, input().split())
aList = list(a)

for y in aList:
    if x > y:
        print(y, end=' ')

#10952
res = []

while True:
    a, b = map(int, input().split())
    res.append(a+b)

    if a == 0 and b == 0:
        del res[-1]
        break

for i in res:
    print(i)

# 10951
# 입력이 끝날 때까지 A+B를 출력하는 문제
'''
# 1110
a = input()

if len(a) == 1:
    a = "0"+a

print("a:", a)

sum = int(a[0]) + int(a[1])
print("sum:", sum)

b = str(sum)
print("b:", b)

new = a[-1] + b[-1]
print("new:", new)

c = new
print("c:", c)
# 내일 다시

