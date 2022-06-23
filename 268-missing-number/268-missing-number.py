class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ln = len(nums)
        # flags = [True] * ln
        
        c = 0
        for i in range(ln + 1):
            if i not in nums:
                c = i
        return c
                
                