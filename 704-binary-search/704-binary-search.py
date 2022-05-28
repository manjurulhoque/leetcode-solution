class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        x = target
        while low <= high:

            mid = low + (high - low)//2

            if nums[mid] == x:
                return mid

            elif nums[mid] < x:
                low = mid + 1

            else:
                high = mid - 1

        return -1