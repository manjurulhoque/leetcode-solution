class Solution:
    def findDiscount(self, i, n, prices) -> int:
        for j in range(i + 1, n):
            if j > i and prices[j] <= prices[i]:
                return prices[j]
        return 0
            
    def finalPrices(self, prices: List[int]) -> List[int]:
        ln = len(prices)
        res = []
        
        for i in range(ln):
            #for j in range(i + 1, ln):
            res.append(prices[i] - self.findDiscount(i, ln, prices))
            
        return res
        