class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        r = 0
        
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                r += 1
        
        return r