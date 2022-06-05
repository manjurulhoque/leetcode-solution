class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 0
            
        values = list(d.values())
        #print(values)
        values.sort()
        mx = values[-1]
        return all([value == mx for value in values])