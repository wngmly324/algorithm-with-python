# 10818
n = int(input())
a = list(map(int, input().split()))

print(min(a), max(a))

# 2562
count = 0
res = []
while count < 9:
    count += 1
    n = int(input())
    res.append(n)

print(max(res))
print(res.index(max(res))+1)

# 2577
a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
sMul = str(mul)
sMulList = list(sMul)

for i in range(0,10):
    print(sMulList.count('%d' % i))

# 3052
count = 0
res = []
while True:
    count += 1
    n = int(input())
    rest = n % 42
    res.append(rest)

    if count == 10: break

count2 = 0
for i in range(42):
    if i in res:
        count2 += 1
    else: continue

print(count2)

# 1546
n = int(input())
score = list(map(int, input().split()))

maxScore = max(score)

fakeScoreList = []
sum = 0

for i in score:
    res = round(i/maxScore*100, 2)
    fakeScoreList.append(res)
    sum += res

print(sum / n)

n = int(input())
while n:
    score = 0
    list = []
    sum = 0

    q = input()

    for i in range(0, len(q)):
        if q[i] == 'O':
            score += 1
            list.append(score)
        elif q[i] == 'X':
            score = 0
            
        i += 1
    
    for j in list:
        sum += j
        
    print(sum)
    n -= 1

# 4344
c = int(input())
while c:
    sum = 0
    count = 0

    s = list(map(int, input().split()))

    for i in range(1, len(s)):
        sum += s[i]
        avg = sum / s[0]

    for j in range(1, len(s)):
        if s[j] > avg:
            count += 1
            
    res = round(count/s[0] * 100, 3)
    print("%0.3f%%" % res)
    
    c -= 1
