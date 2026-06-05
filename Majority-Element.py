1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        counts = Counter(nums)
4        m = len(nums) / 2
5
6        for num, count in counts.items():
7            if count > m:
8                return num