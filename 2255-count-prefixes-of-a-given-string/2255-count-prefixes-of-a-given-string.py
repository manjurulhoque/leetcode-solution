class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefixes = []
        ln = len(s)
        c = 0
        for i in range(ln):
            prefixes.append(s[0:i+1])
        
        for word in words:
            if word in prefixes:
                c += 1
        # print(prefixes)
        return c