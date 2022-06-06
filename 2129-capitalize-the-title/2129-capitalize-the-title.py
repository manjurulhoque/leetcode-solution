class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        return " ".join([word.capitalize() if len(word) > 2 else word.lower() for word in words])