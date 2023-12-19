from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_item = min(prices)
        print("s", prices[-1])


        actual_prices = prices[min_item:]
        print("actual_prices", actual_prices)
        max_profit_price = max(actual_prices)
        return max_profit_price - min_item

obj = Solution()
print(obj.maxProfit([2,4,1]))