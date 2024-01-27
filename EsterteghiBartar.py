#soal4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    a, b = map(int, input().split())

    if a < b:
        x = range(a, b + 1)
    else:
        x = range(b, a + 1)

    prime_numbers = list(filter(is_prime, x))

    if a < b:
        print('main order - amount:', len(prime_numbers))
    elif a == b:
        print('main order - amount:', len(prime_numbers))
    else:
        print('reverse order - amount:', len(prime_numbers))
#clean_code