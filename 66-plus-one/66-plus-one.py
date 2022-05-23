class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''.join([str(x) for x in digits])
        n = int(n) + 1
        return [char for char in str(n)]