class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f, s = -1, -1
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                f = mid
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                s = mid
                l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return [f, s]
                