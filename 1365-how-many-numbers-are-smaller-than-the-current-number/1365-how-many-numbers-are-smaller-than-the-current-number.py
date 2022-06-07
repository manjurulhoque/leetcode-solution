class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n, ln = 0, len(nums)
        smaller = []
        for i in range(ln):
            n = 0
            for j in range(ln):
                if i != j and nums[j] < nums[i]:
                    n += 1
            smaller.append(n)
        
        return smaller
                    
            