def two_sum(nums, target):
    result = []
    lookup = {}
    for i1, num in enumerate(nums):
        if target - num in lookup:
            result.append(lookup[target - num] + i1)
        lookup[num] = i1
    return result
adad = [int(i) for i in input().split()]
n = int(input())
for i in sorted(two_sum(adad,n)):
    print(i)
if len(two_sum(adad,n)) == 0:
    print('Not Found!')
#clean_code