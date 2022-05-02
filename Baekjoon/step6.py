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
