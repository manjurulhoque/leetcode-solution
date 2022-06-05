class Solution:
    def countPoints(self, rings: str) -> int:
        out =0
        for i in range(0,10):
            if rings.count('R'+str(i)) and rings.count('G'+str(i)) and rings.count('B'+str(i)):
                out +=1
        return out