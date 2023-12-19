class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occ = {c: i for i, c in enumerate(s)}
        print("last occurence: ", last_occ)
        for i, c in enumerate(s):
            print("i: ", i)
            print("c: ", c)

            if c not in seen:

                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
                print("seen: ", seen)
                print("stack: ", stack)
        return ''.join(stack)

obj = Solution()
s = "bcabc"
print("res: ", obj.removeDuplicateLetters(s=s))
print("a" < "c")