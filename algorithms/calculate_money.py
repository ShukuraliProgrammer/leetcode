class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        start = 1
        end = 8
        while n > 7:

            for i in range(start, end):
                print("i: ", i)
                res += i
            start += 1
            end += 1
            n = n - 7

        print("res: ", res)

        for i in range(n):
            print("start: ", start)
            res += start
            start += 1
        print("res1: ", res)
        return res

obj = Solution()
print(obj.totalMoney(20))
