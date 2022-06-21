class Solution:
    def checkRecord(self, s: str) -> bool:
        if 'LLL' in s:
            return False
        total_absent = 0

        length = len(s)
        for i in range(length):
            c = s[i]
            if c == 'A':
                total_absent += 1
        
        return total_absent < 2
            