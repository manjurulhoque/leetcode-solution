1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        return len(nums) != len(list(set(nums)))