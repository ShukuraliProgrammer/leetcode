def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                continue


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 15
print(twoSum(nums, target))