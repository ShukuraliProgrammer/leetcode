
def find_large_positive_integer(nums):

    pos = []

    for i in nums:
        if -(i) in nums:
            pos.append(abs(i))
    if len(pos) > 0:
        return max(pos)
    return 0

res = find_large_positive_integer(nums=[-10,8,6,7,-2,-3])
print(res)