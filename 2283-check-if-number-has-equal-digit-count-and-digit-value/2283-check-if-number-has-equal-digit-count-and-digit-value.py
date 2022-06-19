class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            # count = num.count(str(i))
            if num.count(str(i)) != int(num[i]):
                return False
            else:
                continue    
        return True