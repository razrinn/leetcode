from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        length = len(prices)

        if length <= 1:
            return 0
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if sell >= buy:
                r+=1
                res = max(res, sell - buy)
            else:
                l += 1
                if l == r:
                    r += 1

        return res
