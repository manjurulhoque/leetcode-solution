class Solution:
    def sol(self, n) -> int:
        p = 0
        m = str(n)
        # print(m)
        for i in range(len(m)):
            p += int(m[i])
        print(p)
        if len(str(p)) == 1:
            return p
        else:
            return self.sol(p)
    
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        
        return self.sol(num)