from re import *


with open("C:/Users/Ivan228/Downloads/2400.txt") as f:
    s = f.readline()
pattern1 = "PNO"
pattern2 = "NPO"
repl1 = '1'
repl2 = '2'
match1 = sub(pattern1, repl1, s)
match2 = sub(pattern2, repl2, match1)
a = findall("1*|2*", match2)
print(a)

