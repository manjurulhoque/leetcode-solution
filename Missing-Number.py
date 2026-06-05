1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n = len(nums)
4        nums.sort()
5
6        for i in range(0, n + 1):
7            if i not in nums:
8                return i
9        return 0