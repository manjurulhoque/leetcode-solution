class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz"
        d = {}
        for i in range(len(letters)):
            d[letters[i]] = 0
        for i in range(len(sentence)):
            d[sentence[i]] += 1
        
        return all(value != 0 for value in d.values())