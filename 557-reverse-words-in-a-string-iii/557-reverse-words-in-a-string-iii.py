class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = []
        words = s.split(" ")
        for word in words:
            new_s.append(word[::-1])
        return " ".join(new_s)