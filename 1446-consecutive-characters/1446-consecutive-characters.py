class Solution:
    def maxPower(self, s: str) -> int:
        power = []
        n = 0
        
        for i in range(len(s)):
            # n = 1
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    n += 1
                else:
                    break
                    
            power.append(n)
            n = 0
            
        return max(power)