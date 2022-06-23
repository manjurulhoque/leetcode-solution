class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        
        c = 0
        while True:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            
            c += 1
            print(num1, num2)
            if num1 == 0 or num2 == 0:
                break
                
        return c