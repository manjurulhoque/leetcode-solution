class Solution:
    def isThree(self, n: int) -> bool:
        c = 1
        
        for i in range(1, int(n / 2) + 1):
            if n % i == 0:
                c += 1
        
        return c == 3