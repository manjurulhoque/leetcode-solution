class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        
        while num > 0:
            if num % 2 == 0:
                step += 1
                num = int(num / 2)
            else:
                step += 1
                num -= 1
        return step