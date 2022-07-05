class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx, cur = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                cur = 0
            mx = max(cur, mx)
        return mx