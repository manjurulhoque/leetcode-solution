class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        result = ""
        for i in range(l):
            result += word1[i]
            result += word2[i]
        
        result += word1[l:]
        result += word2[l:]
        return result