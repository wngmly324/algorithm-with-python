# 11654
a = input()
print(ord(a))

# 11720
n = int(input())
a = input()

sum = 0

for i in range(len(a)):
    sum += int(a[i])

print(sum)

# 10809
s = input()
alpha = []

for i in range(97,123):
    alpha.append(chr(i))

for j in alpha:
    if j in s:
        print(s.index(j) , end=' ')
    else:
        print(-1, end=' ')

# 2675
t = int(input())
while t:
    s = list(input())
    r = int(s[0])

    for i in range(2, len(s)):
        print(s[i] * r, end='')
        
    print( )
    
    t -= 1

# 1157
s = input()
ss = s.lower()
alpha = []

count = 0
res = []

for i in range(97,123):
    alpha.append(chr(i))

for j in alpha:
    if j in ss:
        res.append(ss.count(j))
    else:
        res.append(0)
        
maxNum = max(res)
index = res.index(maxNum)

if res.count(maxNum) > 1:
    print("?")
else:
    print(alpha[index].upper())

# 1152
a = list(input().split(' '))

if a[0] == '':
    del a[0]

    if a[-1] == '':
        del a[-1]
    print(len(a))
elif a[-1] == '':
    del a[-1]
    print(len(a))
else:
    print(len(a))

# 2908
a, b = input().split(' ')

aa = a[2] + a[1] + a[0]
bb = b[2] + b[1] + b[0]

if int(aa) > int(bb):
    print(aa)
else:
    print(bb)

# 5622
a = input()
sum = 0
for i in a:
    if i in ['A','B','C']:
        time = 3
        sum += time
    elif i in ['D','E','F']:
        time = 4
        sum += time
    elif i in ['G','H','I']:
        time = 5
        sum += time
    elif i in ['J','K','L']:
        time = 6
        sum += time
    elif i in ['M','N','O']:
        time = 7
        sum += time
    elif i in ['P','Q','R','S']:
        time = 8
        sum += time
    elif i in ['T','U','V']:
        time = 9
        sum += time
    elif i in ['W','X','Y','Z']:
        time = 10
        sum += time
        
print(sum)

# 2941
a = input()

x = ['c=','c-','dz=','d-','lj','nj','s=','z=']
y = []
for i in x:
    xCnt = a.count(i)
    y.append(xCnt)

sum = 0
for j in y:
    sum += j

aLen = len(a)
print(aLen - sum)

# 1316
n = int(input())
cnt = n

while n:
    a = input()
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            pass
        elif a[j] in a[j+1:]:
            cnt -= 1
            break
    n -= 1
    
print(cnt)
