from typing import List
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = min(prices)
        prices.remove(first)
        second = min(prices)
        if first+second<=money:
            print(first, second)
            return money - (first+second)
        return money

obj = Solution()
print(obj.buyChoco([98,54,6,34,66,63,52,39], 62))