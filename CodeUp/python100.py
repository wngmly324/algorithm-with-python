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
'''

