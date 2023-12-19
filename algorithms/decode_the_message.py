class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        matched_key = key.replace(" ", "")
        unique_key = set(matched_key)
        sorted_list = sorted(unique_key)
        print("sorted list", sorted_list)
        converted_string = str(unique_key)
        print("converted string", converted_string)
        res = []
        for lett in message:
            print("lett", lett)
            if lett == " ":
                res.append(" ")
            index = converted_string.index(lett)
            real_letter = chr(index)
            print("real letter", real_letter)
            res.append(real_letter)
        return " ".join(res)

obj = Solution()

res = obj.decodeMessage(key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv")

print(res)