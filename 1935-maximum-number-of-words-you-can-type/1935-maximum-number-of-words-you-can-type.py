class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        c = 0
        # print(words)
        for word in words:
            flag = True
            for letter in brokenLetters:
                # print(letter)
                if word.count(letter) == 0:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                c += 1
            
        return c