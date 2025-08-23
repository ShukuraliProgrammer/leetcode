class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        start_bin = str(bin(start)[2:])
        goal_bin = str(bin(goal)[2:])
        for i in range(len(start_bin)):
            for j in goal_bin[::-1]:
                if i == j:
                    continue
                else:
                    pass
            pass


obj = Solution()
obj.minBitFlips(10, 7)