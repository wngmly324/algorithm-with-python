# 15596
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

# 4673
num = set(range(1,10001))

def no(n):
    sNum = str(n)
    sNumList = []
    for i in range(len(sNum)):
        sNumList.append(sNum[i])

    sum = n
    for i in sNumList:
        sum += int(i)

    return sum

noSelfList = []
for j in num:
    noSelfNum = no(j)
    noSelfList.append(noSelfNum)

noSet = set(noSelfList)

result = num.difference(noSet)

resList = list(result)
resList.sort()

for k in resList:
    print(k)

# 1065
num = int(input())

def hansu(n):
    cnt = 0

    for i in range(1, num+1):
        if i < 100:
            cnt += 1
        elif i >= 100:
            sNum = str(i)
            sList = []

            for j in range(len(sNum)):
                sList.append(sNum[j])

            if int(sList[1])-int(sList[0]) == int(sList[2]) - int(sList[1]):
                cnt += 1
            else: pass

        i += 1
            
    return cnt

print(hansu(num))
