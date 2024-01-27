#soal1mosallaspaskal
a = int(input())
def binomial(n, r):
    p = 1    
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p
for row in range(a):
    for k in range(row + 1):
        print(binomial(row, k), end=' ', flush=True) 
    print()
#clean_code