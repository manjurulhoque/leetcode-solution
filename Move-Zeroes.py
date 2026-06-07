1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n = len(nums)
7        k = 0
8
9        for i in range(n):
10            if nums[i] != 0:
11                nums[k], nums[i] = nums[i], nums[k]
12                k += 1
13        