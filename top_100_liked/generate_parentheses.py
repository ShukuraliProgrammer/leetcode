from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        results = []
        def add_parenthesis(opened: int, closed: int) -> None:
            if opened == closed == n:
                results.append("".join(stack))

                return
            if opened > closed:
                stack.append(")")
                add_parenthesis(opened, closed + 1)
                stack.pop()
            if opened < n:
                stack.append("(")
                add_parenthesis(opened + 1, closed)
                stack.pop()

        add_parenthesis(0, 0)


        return results



obj = Solution()
print(obj.generateParenthesis(3))
