class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        max_length = 0
        seen = {}
        for right_pointer in range(len(s)):
            char = s[right_pointer]
            if char in seen and seen[char] >= left_pointer:
                left_pointer = seen[char] + 1
            else:
                max_length = max(max_length, right_pointer - left_pointer + 1)
            seen[char] = right_pointer
        return max_length










obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))
