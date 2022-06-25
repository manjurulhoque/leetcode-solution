class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         d = dict()
        
#         for i in range(len(s)):
#             k = 0
#             d[s[i]] = -1
#             for j in range(k, len(t)):
#                 if s[i] == t[j]:
#                     d[s[i]] = j
#                     k = j
#                     break
#         print(d)
#         l = list(d.values())
#         if -1 in l:
#             return False
#         return all(l[i] <= l[i+1] for i in range(len(l) - 1))
#         # return True
        i, j  = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
                    