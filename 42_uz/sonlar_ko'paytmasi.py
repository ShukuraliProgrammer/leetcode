def productExceptSelf(nums: list) -> list:
    res = []
    def multiple_items(items: list):
        print(items)
        multiple = 1
        for num in items:
            multiple *= num
        return multiple

    for j in range(len(nums)):
        res.append(multiple_items(nums[:j]+nums[j+1:]))
    return res

print(productExceptSelf([-1,1,0,-3,3]))