class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        s = "".join(s1)
        t1 = sorted(t)
        t = "".join(t1)
        return s == t