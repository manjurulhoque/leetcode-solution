class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = []
        
        for n in nums:
            if nums.count(n) > 1:
                pass
            else:
                res.append(n)
        return sum(res)