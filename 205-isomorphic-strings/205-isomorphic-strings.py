class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ln1, ln2 = len(s), len(t)
        if ln1 != ln2:
            return False
        
        dict1, dict2 = dict(), dict()
        flag = True
        
        for i in range(ln1):
            if not dict1.get(s[i]):
                dict1[s[i]] = t[i]
            else:
                if dict1.get(s[i]) != t[i]:
                    flag = False
                    break
                else:
                    dict1[s[i]] = t[i]
        # flag = True
        for i in range(ln1):
            if not dict2.get(t[i]):
                dict2[t[i]] = s[i]
            else:
                if dict2.get(t[i]) != s[i]:
                    flag = False
                    break
                else:
                    dict2[t[i]] = s[i]
        return flag
#         list1 = list(s)
#         for i in range(len(list1)):
#             list1[i] = t[i]
        
#         return "".join(list1) == t