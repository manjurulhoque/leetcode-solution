class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
#         index = -1
#         left, right = 0, 0
        
#         for i in range(len(nums)):
#             if sum(nums[:i]) == sum(nums[i + 1:]):
#                 index = i
#                 break
        
#         return index
        sm = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (sm - leftsum - x):
                return i
            leftsum += x
        return -1