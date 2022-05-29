class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = 2 ** 31 -1
        while l < r:
            mid = (l + r) / 2
            ans = mid * mid
            if ans == num:
                return True
            if ans > num:
                r = mid - 1
            else:
                l = mid + 1
        if l * l == num:
            return True
        return False