#soal 3
a = list(bin(int(input()))[2:])
b = list(bin(int(input()))[2:])
c = int(input())
if len(a) < 32:
    for num in range(32 - len(a)):
        a.insert(0, '0')
if len(b) < 32:
    for numb in range(32 - len(b)):
        b.insert(0, '0')
d = b + a
a1 = []
for i in range (1, c+1):
    a1.append(input())
for i in a1:
    if d[63-int(i)] == '0':
        print('no')
    else:
        print('yes')
#clean_code