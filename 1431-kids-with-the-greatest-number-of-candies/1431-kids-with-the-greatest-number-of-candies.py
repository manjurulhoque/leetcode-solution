class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = sorted(candies, reverse=True)[0]
        out = []
        
        for can in candies:
            if can + extraCandies >= mx:
                out.append(True)
            else:
                out.append(False)
        return out