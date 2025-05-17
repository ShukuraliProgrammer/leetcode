def moveZeroes(nums: list) -> list:
    zero_counter = 0
    for i in nums:
        if i == 0:
            nums.remove(0)
            zero_counter += 1

    for z in range(zero_counter):
        nums.append(0)
    return nums

print(moveZeroes([0, 0, 0, 0, 1]))