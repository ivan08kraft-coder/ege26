from re import *

with open("2416.txt") as f:
    s = f.readline()
l = []
for i in finditer("([AE][BCD])+", s):
    l.append(i[0])
print(len(max(l, key=len))//2)
