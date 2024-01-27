a = int(input())
b = int(input())
c = int(input())
while b != 0:
    data = a & b
    a = a ^ b
    b = data << 1
print(a)
if a == c :
    print('YES')
else:
    print('NO')
#clean_code