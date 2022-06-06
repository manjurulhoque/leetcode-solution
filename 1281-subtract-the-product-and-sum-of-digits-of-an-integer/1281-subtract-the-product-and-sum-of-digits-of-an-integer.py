class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p_d, s_d = 1, 0
        
        while n > 0:
            m = n % 10
            p_d *= m
            s_d += m
            n = n // 10
            
        return p_d - s_d