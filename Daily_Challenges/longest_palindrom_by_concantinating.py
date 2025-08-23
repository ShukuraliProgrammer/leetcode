from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        palindrom_list = []
        last_word = ""
        l = len(words)
        words_set = set(words)
        for i in range(l):
            if words[i][::-1] in words_set:
                print(words[i], palindrom_list)
                if not palindrom_list:
                    palindrom_list.append(words[i])
                    palindrom_list.append(words[i][::-1])
                    last_word = words[i]

                else:
                    print('W', words[i])
                    last_word_index = words.index(last_word) + 1
                    if words[i] == words[i][::-1]:
                        palindrom_list[last_word_index:last_word_index] = [words[i]]
                    palindrom_list[last_word_index:last_word_index] = [words[i], words[i][::-1]]
                words.remove(words[i])
                words.remove(words[i][::-1])
        print(palindrom_list)
        return len("".join(palindrom_list))


obj = Solution()
print(obj.longestPalindrome(["lc", "cl", "gg"]))

