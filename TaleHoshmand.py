def number_to_base(n, b):
    if 2 <= b <= 9:
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(n % b)
            n //= b
        digits = digits[::-1]
        kh = sum(x * 10 ** (len(digits) - 1 - k) for k, x in enumerate(digits))
        return kh
    else:
        return 0

n_values = []
b_values = []

while True:
    n, b = map(int, input().split())
    n_values.append(n)
    b_values.append(b)
    if n == -1:
        break

n_values.remove(-1)
b_values.remove(-1)

invalid_base = any(2 > d or d > 9 for d in b_values)

if not invalid_base:
    result = sum(number_to_base(sum(j for j in range(1, i + 1) if i % j == 0), b_values[i])
                 for i in range(len(n_values)))
    print(result)
else:
    print('Invalid base!')
#clean_code