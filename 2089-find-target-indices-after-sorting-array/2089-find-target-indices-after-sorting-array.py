class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lst = []
        nums.sort()
        for i in range(len(nums)):
            if target == nums[i]:
                lst.append(i)
        return lst