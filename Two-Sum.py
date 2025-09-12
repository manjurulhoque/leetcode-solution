class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if (n + m) == target and i != j:
                    return [i, j]
        return []