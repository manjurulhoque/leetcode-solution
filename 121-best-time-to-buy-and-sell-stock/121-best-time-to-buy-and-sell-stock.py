class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer
        l, r = 0, 1
        mx = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                mx = max(mx, (prices[r] - prices[l]))
            else:
                l = r
            r += 1
        
        return mx