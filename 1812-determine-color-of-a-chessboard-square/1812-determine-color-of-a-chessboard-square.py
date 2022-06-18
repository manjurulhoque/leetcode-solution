class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        d = {
            'a': [2, 4, 6, 8],
            'b': [1, 3, 5, 7],
            'c': [2, 4, 6, 8],
            'd': [1, 3, 5, 7],
            'e': [2, 4, 6, 8],
            'f': [1, 3, 5, 7],
            'g': [2, 4, 6, 8],
            'h': [1, 3, 5, 7],
        }
        l = d[coordinates[0]]
        return int(coordinates[1]) in l