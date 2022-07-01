class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = 0
        
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                n += 1
        
        return n