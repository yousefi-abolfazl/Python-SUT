nums = int(input())  # تعداد ستون‌ها
lstw = []  # لیست کلمات R,L,B
x_lst = [0]  # لیست موقعیت‌های لمس شده
y_lst = []

# دریافت ورودی‌ها
while True:
    word = input()
    lstw.append(word)
    if word == 'END':
        break

lstw.remove('END')

# محاسبه موقعیت‌ها
for i, w in enumerate(lstw):
    if w == 'R':
        x_now = min(i + 1, nums - 1)
    elif w == 'L':
        x_now = max(i - 1, 0)
    elif w == 'B':
        y_lst.append(x_now)
        x_lst.extend(['T', x_now])

# چاپ نمودار
for i in range(x_lst.count('T') + 1):
    x_lst1 = sorted(set(filter(lambda x: x != 'T', x_lst)), key=abs)
    spaces = ' . ' * x_lst1[0]
    stars = ' * ' * len(x_lst1)
    dots = ' . ' * (nums - x_lst1[-1] - 1)
    print(f"{spaces}{stars}{dots}".strip())
    x_lst = x_lst[x_lst.count('T') + 1:]

# چک کردن خروجی ممکن
if nums - 1 in set(x_lst) and x_now == nums - 1:
    print('There\'s no way out!')
#clean_code