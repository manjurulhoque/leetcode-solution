class Solution:
    def replaceDigits(self, s: str) -> str:
        ln = len(s)
        ss = []
        for i in range(ln):
            a = s[i]
            if a.isnumeric():
                aa = s[i - 1]
                ns = chr(ord(aa) + int(a))
                ss.append(ns)
            else:
                ss.append(a)
            
        return ''.join(ss)
                