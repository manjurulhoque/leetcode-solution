class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        d = {a: 0 for a in range(26)}
        for i in range(len(s)):
            d[ord(s[i]) - 97] += 1
        
        while len(s) != len(res):
            for i in range(26):
                if d[i] > 0:
                    res += chr(ord('a') + i)
                    d[i] -= 1
            
            for i in range(25, -1, -1):
                if d[i] > 0:
                    res += chr(ord('a') + i)
                    d[i] -= 1
        
        return res
        
        