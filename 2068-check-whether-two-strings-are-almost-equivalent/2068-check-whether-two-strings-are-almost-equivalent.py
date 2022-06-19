class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1_dict = dict(collections.Counter(word1))
        word2_dict = dict(collections.Counter(word2))
        #print(word1_dict)
        #print(word2_dict)
        word1, word2 = False, False
        for key, value in word1_dict.items():
            if abs(word2_dict.get(key, 0) - value) <= 3:
                continue
            else:
                return False
        word1 = True
        for key, value in word2_dict.items():
            if abs(word1_dict.get(key, 0) - value) <= 3:
                continue
            else:
                return False
        word2 = True
        
        return word1 and word2
            