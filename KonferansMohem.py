import re
l = 0
n = int(input())
damane = []
emails = []
b = []
while l < n:
    emails.append(input())
    l += 1

for i in emails:
    t = list(i)
    for j in range(len(t)):
        if  t[0] != '@':
            t.pop(0)
        else:
            t.pop(0)
            break
    h = ''
    for k in t:
        h += k
    b.append(h)
b = sorted(list(set(b)))
for i in b:
    print(i)
#clean_code 