1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        nums.sort()
4
5        for i in range(len(nums) - 1):
6            if nums[i] == nums[i + 1]:
7                return True
8        return False