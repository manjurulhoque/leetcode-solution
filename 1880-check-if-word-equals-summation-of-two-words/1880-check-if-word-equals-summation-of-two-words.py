class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f_sum, s_sum, t_sum = "", "", ""
        
        for word in firstWord:
            f_sum += str(ord(word) - ord('a'))
        for word in secondWord:
            s_sum += str(ord(word) - ord('a'))
        for word in targetWord:
            t_sum += str(ord(word) - ord('a'))
        
        return int(f_sum) + int(s_sum) == int(t_sum)