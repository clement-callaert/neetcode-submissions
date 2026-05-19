class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell, min_buy = 0, float('inf')
        for i, price in enumerate(prices):
            min_buy = min(min_buy, price)
            max_sell = max(max_sell, price - min_buy)

        return max_sell
