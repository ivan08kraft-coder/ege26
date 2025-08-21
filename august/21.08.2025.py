from re import *
with open("24-347.txt") as f:
    s = f.readline()
num = []
for i in finditer(r"[1-7][0-7]*", s):
    num.append(i[0])
num1 = []
for i in num:
    if a % 13 == 0:
        num1.append(a)
    else:
        for i1 in range(0, len(i)):
            for i2 in range(1, len(i) - i1):
                if int(i[i1:-i2]) % 13 == 0:
                    num1.append(a)

num2 = []
g = len(max(num1, key=len))
for i in num1:
    if len(str(i)) == g:
        num2.append(int(i))

print(num2)
