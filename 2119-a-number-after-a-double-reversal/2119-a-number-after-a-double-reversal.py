class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        return num == int(str(int(s[::-1]))[::-1])