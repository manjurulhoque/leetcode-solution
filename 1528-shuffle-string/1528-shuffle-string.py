class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ''
        t = [a for a in s]
        for i in range(len(s)):
            t[indices[i]] = s[i]
        return "".join(t)