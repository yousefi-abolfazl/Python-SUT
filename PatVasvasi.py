matn = input()

# حذف '@' و '#' اضافی
t = list(matn)
l = t.count('@')
for _ in range(l):
    for i in range(len(t)):
        if t[len(t) - i - 1] == '#':
            t.pop(len(t) - i - 1)
            break

# حذف فاصله‌های اضافی
t = ' '.join(t).split()
t = ''.join(t).strip()

# جایگزینی '\n' با فاصله
t = t.replace('\n', ' ')

# چاپ متن فرمت‌دار
print('Formatted Text:', end='')
for i1, i in enumerate(t):
    if i1 in p:
        print(f' {i}', end='' if i.isspace() else '\n')
    else:
        print(i, end='')
#clean_code