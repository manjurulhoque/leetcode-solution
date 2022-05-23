class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        while s != 1 and s != 4:
            s = 0
            while n > 0:
                m = (n % 10)
                n = floor(n / 10)
                s += (m * m)
            n = s
        return s == 1
        