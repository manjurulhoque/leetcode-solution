class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        
        while num:
            m = num % 10
            digits.append(m)
            
            num //= 10
        digits.sort()
        
        mn = min((digits[0] * 10 + digits[2] + digits[1] * 10 + digits[3]), (digits[0] * 10 + digits[3] + digits[1] * 10 + digits[2]))
        return mn