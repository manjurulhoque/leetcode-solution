class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] == target:
                return i
            if i < l -1 and target > nums[i] and target < nums[i+1]:
                return i+1
            if target < nums[i]:
                return i
            elif i == l - 1:
                return l