class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        sentence = [w for w in words]
        for word in words:
            index = int(word[-1]) - 1
            sentence[index] = word[0:-1]
        return " ".join(sentence)