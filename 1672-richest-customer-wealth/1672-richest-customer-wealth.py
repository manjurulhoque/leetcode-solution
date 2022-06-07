class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        
        for ac in accounts:
            wealth.append(sum(ac))
        
        return max(wealth)