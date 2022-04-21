# 1330
a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

# 9498
score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 2753
year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print("1")
elif year % 4 == 0 and year % 400 == 0:
    print("1")
else:
    print("0")

# 14681
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")

# 2884
H, M = map(int, input().split())
if H == 0:
    if M >= 45:
        print(H, M-45)
    else:
        print(H+24-1, M+15)
elif M >= 45:
    print(H, M-45)
elif M < 45:
    print(H-1, M+15)

# 2525
H, M = map(int, input().split())
ovenTime = int(input())

H += ovenTime // 60
M += ovenTime % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
    
print("%d %d" % (H, M))
    
# 2480
a, b, c = map(int, input().split())
if a == b and b == c and c == a:
    print(10000+a*1000)
elif a != b and b != c and c != a:
    if a > b and a > c:
        print(a*100)
    elif b > a and b > c:
        print(b*100)
    else:
        print(c*100)
else:
    if a == b and b != c:
        print(1000+a*100)
    elif a != b and a == c:
        print(1000+a*100)
    elif b == c and c != a:
        print(1000+b*100)
