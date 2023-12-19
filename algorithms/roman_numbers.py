class Solution:
    def romanToInt(self, s: str) -> int:
        s_list = list(s.split(" "))
        print("s:", s_list)
        res = 0
        for i in s:

            print("id", i)
            match i:
                case "I":
                    res += 1
                case "V":
                    res += 5
                case "X":
                    res += 10
                case "L":
                    res += 50
                case "C":
                    res += 100
                case "D":
                    res += 500
                case "M":
                    res += 1000

        return res

obj = Solution()
print(obj.romanToInt("MCMXCIV"))
