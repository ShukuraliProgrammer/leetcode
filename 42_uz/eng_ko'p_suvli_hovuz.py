def maxArea(nums: list) -> int:
    if len(nums) == 1:
        return 0
    max_area = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            index_dec = j-i
            if nums[i] < nums[j]:
                sum_are = index_dec * nums[i]
            else:
                sum_are = index_dec * nums[j]
            max_area = max(max_area, sum_are)
    return max_area


nums_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(nums_list))
