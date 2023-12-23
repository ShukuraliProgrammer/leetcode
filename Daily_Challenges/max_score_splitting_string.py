class Solution:
    def maxScore(self, s: str) -> int:
        right = list(map(int, s))
        left = []
        res = []
        for i in range(len(s)-1):
            left.append(right.pop(0))
            res.append(right.count(1) + left.count(0))
        return max(res)

s = Solution()
print(s.maxScore("00111"))
