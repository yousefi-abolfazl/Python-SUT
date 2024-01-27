import re
a = []
b = []
#words = '!10 o4 g6 l3 l2 u7 H0 /5 y8 e1 s9'
t = re.split('\s', input())
l = 0
for i in range(len(t)):
    c = t[0]
    c1 = list(c)
    a.append(c1[0])
    c1.pop(0)
    for j1,j in enumerate(c1):
        l += int(j) * 10 ** (len(c1)-j1-1)
    b.append(l)
    l = 0
    t.pop(0)
a_copy = a.copy()
for i1, i in enumerate(a):
    a_copy[int(b[i1])] = a[i1]
for i in a_copy:
    print(i, end= '')
#clean_code