from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    new_list = []
    for i in range(len(nums)//2):
        new_list.append(nums[:n][i])
        new_list.append(nums[n:][i])

    return new_list


nums = [1,2,3,4,4,3,2,1]
n = 4
res = shuffle(nums, n)
print("res: ", res)