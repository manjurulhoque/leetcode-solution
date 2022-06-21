class Solution:
    def isSelfDividingNumber(self, n: int) -> bool:
        #print(n)
        main = n
        while n > 0:
            m = n % 10
            # print(m)
            if m == 0 or main % m != 0:
                return False
            n //= 10
        
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        
        for i in range(left, right + 1):
            if self.isSelfDividingNumber(i):
                l.append(i)
        
        return l