def guess(num, pick):
    if num == pick:
        return 0
    elif num < pick:
        return 1
    elif num > pick:
        return -1



class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while True:
            mid = (left + right) // 2
            guess_num = guess(mid, 6)
            print(guess_num)

            if guess_num == -1:
                right = mid
                continue
            elif guess_num == 1:
                left = mid
                continue
            elif guess_num == 0:
                break

        return mid


res = Solution()
print(res.guessNumber(10))