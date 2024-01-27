def gcd(a, b):
    return a if not b else gcd(b, a % b)

def lcd(a, b):
    return 0 if gcd(a, b) == 0 else (a // gcd(a, b)) * b

def calculate(command, numbers):
    if command == 'max1':
        return max(numbers)
    elif command == 'min1':
        return min(numbers)
    elif command == 'sum1':
        return sum(numbers)
    elif command == 'average1':
        return round(sum(numbers) / len(numbers), 2)
    elif command == 'gcd1':
        lst_gcd = [gcd(i, j) for i in numbers for j in numbers]
        return min(lst_gcd)
    elif command == 'lcd1':
        if len(numbers) > 1:
            lcd_result = lcd(numbers[0], numbers[1])
            for i in range(2, len(numbers)):
                lcd_result = lcd(lcd_result, numbers[i])
            return int(lcd_result)

a = input() + '1'

if a in c:
    numbers = []
    while True:
        i = input()
        numbers.append(int(i))
        if i == 'end':
            break

    numbers.pop()  # حذف آخرین عنصر از لیست

    if len(numbers) > 0:
        result = calculate(a, numbers)
        print(result)
    else:
        print('Invalid input!')
else:
    print('Invalid command')
#clean_code