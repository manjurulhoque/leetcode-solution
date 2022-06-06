class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        c = 0
        for i in range(n):
            c ^= (start + 2 * i)
        return c