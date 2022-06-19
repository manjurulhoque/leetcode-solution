class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answers, positions = list(), list()
        ln = len(s)
        
        for i in range(ln):
            if s[i] == c:
                positions.append(i)
        
        for i in range(ln):
            mn = 999999999
            for j in range(len(positions)):
                mn = min(mn, abs(i - positions[j]))
            answers.append(mn)
        
        return answers