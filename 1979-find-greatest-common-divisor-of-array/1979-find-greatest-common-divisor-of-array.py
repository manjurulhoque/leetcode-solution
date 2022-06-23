class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        x, y = nums[0], nums[-1]
        return math.gcd(x, y)