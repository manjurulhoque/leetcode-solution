1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        s = set(nums)
5        return [i for i in range(1, n + 1) if i not in s]