class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l = 0
        indexes = [0]
        if len(text1) > len(text2):
            min_s = text2
            max_s = text1
        else:
            min_s = text1
            max_s = text2
        for i in min_s:
            index = max_s.find(i)
            print("index: ", index)
            if index==0:
                l += 1
            elif index > 0 and index not in indexes:
                if indexes[-1] < index:
                    l += 1
                    indexes.append(index)
            else:
                continue
        return l

obj = Solution()

print(obj.longestCommonSubsequence(text1="abcba", text2="abcbcba"))
