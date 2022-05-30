'''
# 6001
print("Hello")

# 6002
print("Hello World")

# 6003
print("Hello")
print("World")

# 6004
print("'Hello'")

# 6005
print('"Hello World"')

# 6006
print("\"!@#$%^&*()'")

# 6007
print("\"C:\Download\\'hello'.py\"")

# 6008
print('print("Hello\\nWorld")')

# 6009
x = input()
print(x)

# 6010
x = input()
x = int(x)
print(x)

# 6011
f = input()
f = float(f)
print(f)

# 6012
a = input()
b = input()
a = int(a)
b = int(b)
print(a)
print(b)

# 6013
a = input()
b = input()
print(b)
print(a)

# 6014
f = input()
f = float(f)
print(f)
print(f)
print(f)

# 6015
a, b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

# 6016
c1, c2 = input().split()
print(c2, c1)

# 6017
s = input()
print(s, s, s)

# 6018
a, b = input().split(':')
print(a, b, sep=':')

# 6019
y, m ,d = input().split('.')
print(d, m, y, sep="-")

# 6020
bir, num = input().split('-')
print(bir, num, sep='')

# 6021
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 6022
s = input()
print(s[0:2], s[2:4], s[4:6])

# 6023
h, m, s = input().split(':')
print(m)

# 6024
w1, w2 = input().split()
s = w1 + w2
print(s)

# 6025
a, b = input().split()
c = int(a) + int(b)
print(c)

# 6026
a = input()
b = input()
a = float(a)
b = float(b)
print(a+b)

# 6027
a = input()
n = int(a)
print('%x' % n) # 16진수

# 6028
a = input()
n = int(a)
print('%X' % n) # 16진수

# 6029
a = input()
n = int(a, 16)
print('%o'% n) # 8진수

# 6030
n = ord(input()) # ord(문자): 하나의 문자를 인자로 받고 유니코드 정수를 반환
print(n)

# 6031
c = int(input())
print(chr(c)) # chr(정수): 하나의 정수를 인자로 받고 유니코드 문자를 반환

# 6032
a = int(input())
print(-a)

# 6033
n = ord(input())
print(chr(n+1))

# 6034
a, b = map(int, input().split())
c = a - b
print(c)

# 6035
f1, f2 = map(float, input().split())
m = f1 * f2
print(m)

# 6036
w, n = input().split()
print(w * int(n))

# 6037
n = input()
s = input()
print(int(n) * s)

# 6038
a, b = map(int, input().split())
c = a ** b
print(c)

# 6039
f1, f2 = map(float, input().split())
m = f1 ** f2
print(m)

# 6040
a, b = map(int, input().split())
c = a // b
print(c)

# 6041
a, b = map(int, input().split())
c = a % b
print(c)

# 6042
f = float(input())
print(round(f, 2))

# 6043
f1, f2 = map(float, input().split())
m = round(f1 / f2, 3)
print("%.3f" % m)

# 6044
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("%.2f" % (a/b))

# 6045
a, b, c = map(int, input().split())
sum = a + b + c
avg = round(sum / 3, 2)
print("%d %.2f" % (sum, avg))

# 6046
n = int(input())
print(n<<1)

# 6047
a, b = map(int, input().split())
print(a<<b)

# 6048
a, b = input().split()
a = int(a)
b = int(b)
print(a < b)

# 6049
a, b = input().split()
a = int(a)
b = int(b)
print(a == b)

# 6050
a, b = input().split()
a = int(a)
b = int(b)
print(b >= a)

# 6051
a, b = input().split()
a = int(a)
b = int(b)
print(a != b)

# 6052
n = int(input())
print(bool(n))

# 6053
a = bool(int(input()))
print(not a)

# 6054
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 6055
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 6056
a, b = input().split()
a = int(a)
b = int(b)
if bool(a) != bool(b):
    print(True)
else:
    print(False)

# 6057
a, b = input().split()
a = int(a)
b = int(b)
if bool(a) == bool(b):
    print(True)
else:
    print(False)

# 6058
a, b = input().split()
a = int(a)
b = int(b)
if bool(a) == False and bool(b) == False:
    print(True)
else:
    print(False)

# 6059
a = int(input())
print(~a)

# 6060
a, b = input().split()
a = int(a)
b = int(b)
print(a & b)

# 6061
a, b = input().split()
a = int(a)
b = int(b)
print(a | b)

# 6062
a, b = input().split()
a = int(a)
b = int(b)
print(a ^ b)

# 6063
a, b = input().split()
a = int(a)
b = int(b)
c = (a if a>b else b)
print(int(c))
'
# 6064
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = ((a if a<b else b) if ((a if a<b else b)<c) else c)
print(int(d))

# 6065
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0:
    print(a)
    
if b % 2 == 0:
    print(b)
    
if c % 2 == 0:
    print(c)

# 6066
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0:
    print("even")
else:
    print("odd")
    
if b % 2 == 0:
    print("even")
else:
    print("odd")
    
if c % 2 == 0:
    print("even")
else:
    print("odd")

# 6067
a = int(input())
if a < 0:
    if a % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if a % 2 == 0:
        print("C")
    else:
        print("D")

# 6068
n = int(input())
if n >= 90:
    print("A")
elif n >= 70:
    print("B")
elif n >= 40:
    print("C")
else:
    print("D")

# 6069
a = input()
if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

# 6070
n = int(input())
if n // 3 == 1:
    print("spring")
elif n // 3 == 2:
    print("summer")
elif n // 3 == 3:
    print("fall")
else:
    print("winter")
    
# 6071
n = 1
while n != 0:
    n = int(input())
    if n!= 0:
        print(n)

# 6072
n = int(input())
while True:
    print(n)
    n -= 1
    if n == 0: break

# 6073
n = int(input())
while True:
    n -= 1
    print(n)
    if n == 0: break

# 6074
c = ord(input())
for i in range(97, c+1):
    print(chr(i), end=' ')

# 6075
n = int(input())
cnt = 0
n = n + 1
while n:
    print(cnt)
    cnt += 1
    n -= 1
    
# 6076
n = int(input())
for i in range(n+1):
    print(i)

# 6077
n = int(input())
sum = 0
while n:
    if n % 2 == 0:
        sum += n
    n -= 1

print(sum)

# 6078
s = 'a'
while s != 'q':
    s = input()
    print(s)
    
    if s == 'q': break

# 6079
n = int(input())
sum = 0
cnt = 0
while sum < n:
    cnt += 1
    sum += cnt

print(cnt)

# 6080
n, m = input().split()
n = int(n)
m = int(m)
for i in range(1, n+1):
    for j in range(1, m+1):
        print("%d %d" %  (i, j))

# 6081
n = int(input(), 16)
for i in range(1, 16):
    print("%X*%X=%X" % (n, i, (n*i)))

# 6082
n = int(input())
for i in range(1, n+1):
    if i % 10 == 3:
        print("X", end=" ")
    elif i % 10 == 6:
        print("X", end=" ")
    elif i % 10 == 9:
        print("X", end=" ")
    else:
        print(i, end=" ")

# 6083
r, g, b = map(int, input().split())
cnt = 0
for i in range(r):
    for j in range(g):
        for x in range(b):
            cnt += 1
            print("%d %d %d" % (i, j, x))
print(cnt)

# 6084
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
result = round(h * b * c * s / 8 / 1024 / 1024, 1) # 8bit = 1byte, 1024 byte = 1KB, 1024KB = 1MB

print(str(result)+" MB")

# 6085
w, h, b = map(int, input().split())
result = w * h * b / 8 / 1024 / 1024
print("%.2f MB" % result)

# 6086
n = int(input())

i = 0
sum = 0
while sum < n:
    i += 1
    sum += i
    
print(sum)

# 6087
n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    print(i, end=" ")

# 6088
a, d, n = map(int, input().split())
while n-1:
    n -= 1
    a += d

print(a)

# 6089
a, r, n = map(int, input().split())
while n-1:
    n -= 1
    a *= r

print(a)

# 6090
a, m , d , n = map(int, input().split())
while n-1:
    n -= 1
    a = a * m + d
    
print(a)
'''
