class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        ln = len(nums)
        for i in range(ln):
            for j in range(i+1, ln):
                if nums[i] == nums[j]:
                    c += 1
                    
        return c