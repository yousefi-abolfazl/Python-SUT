def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

class Octopus:
    def __init__(self, dna):
        if dna.endswith('s') and dna[-2] != 'b' and dna[0] != 's':
            dna = dna[::-1]
        self.dna = list(dna)
        self.process_octopus_dna()

    def process_octopus_dna(self):
        num = 0
        for index, letter in enumerate(self.dna):
            if index == len(self.dna) - 1 or index == len(self.dna) - 2:
                continue
            if self.dna[index] == self.dna[index + 1] == self.dna[index + 2]:
                num += 1
        for index in range(len(self.dna) - 1, -1, -1):
            if index == len(self.dna) - 1 or index == len(self.dna) - 2:
                continue
            if self.dna[index] == 'x':
                self.dna.append(str(index))
            if self.dna[index] == self.dna[index + 1] == self.dna[index + 2]:
                if num % 3 != 0 and self.dna[index] != 'x':
                    num += 1
                    continue
                for i in range(3):
                    self.dna.pop(index)
                self.dna.insert(index, '(0_0)')
        return print(''.join(self.dna))

class Crab:
    def __init__(self, dna):
        if dna.endswith('m') and dna[0] != 'm':
            dna = dna[::-1]
        self.dna = list(dna)
        self.dna += self.dna[0:10]
        self.process_crab_dna()

    def process_crab_dna(self):
        num = 0
        for index in self.dna:
            if index == 't':
                num += 1
        for index in range(len(self.dna) - 1, -1, -1):
            if index == len(self.dna) - 1:
                continue
            if num % 2 != 0 and self.dna[index] == 't' and self.dna[index + 1] == 't':
                num += 1
                continue
            if self.dna[index] == 't' and self.dna[index + 1] == 't':
                self.dna.pop(index)
                self.dna.pop(index)
                self.dna.insert(index, 'o')
        self.a = ''.join(self.dna)

    def get_result(self
#clean_code