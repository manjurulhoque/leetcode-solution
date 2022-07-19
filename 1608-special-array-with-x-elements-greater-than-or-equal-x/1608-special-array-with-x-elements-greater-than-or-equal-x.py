class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_len = max(nums)
    
        for i in range(1, max_len + 1):
            count = 0
            for num in nums:
                if num >= i:
                    count += 1

            if count == i:
                return i

        return -1