import numpy as np

filename = 'input9.txt'

# خواندن ماتریس از فایل
with open(filename, 'r') as file:
    lines = file.readlines()

n, m = map(int, lines[0].split())
matrix_lines = lines[1:]

# تبدیل رشته‌های ورودی به ماتریس numpy
matrix = [list(map(int, line.split())) for line in matrix_lines]

# حاصلضرب ماتریس‌ها
max_det = float('-inf')
max_det_matrix = None

for i in range(len(matrix) - 1):
    a = np.array(matrix[i])
    b = np.array(matrix[i + 1])
    result = np.linalg.det(np.dot(a, b))
    
    if result > max_det:
        max_det = result
        max_det_matrix = (a, b)

# ماتریس حاصل ضرب با بیشترین متغیرهای مستقل
final_matrix = max_det_matrix[0].dot(max_det_matrix[1])

# معکوس ماتریس
inv_final_matrix = np.linalg.inv(final_matrix)

# گرد کردن اعداد
inv_final_matrix_rounded = np.round(inv_final_matrix, 3)

# چاپ معکوس ماتریس
for row in inv_final_matrix_rounded:
    print(' '.join(map(str, row)))
#clean_code