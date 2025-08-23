def leftRightDifference(nums: list) -> list:
    result = []
    for i in range(len(nums)):
        left_trainer = sum(nums[:i])
        right_trainer = sum(nums[i+1:])
        print(left_trainer, right_trainer)
        if left_trainer > right_trainer:
            result.append(-1)
        elif left_trainer < right_trainer:
            result.append(1)
        elif left_trainer == right_trainer:
            result.append(0)

    return result


print(leftRightDifference([1, 2, 3, 4, 5]))



