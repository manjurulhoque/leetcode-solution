class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells = s.split(":")
        cell1, cell2 = cells[0], cells[1]
        n, m = int(cell1[-1]), int(cell2[-1])
        l = []
        cell1_c, cell2_c = cell1[0], cell2[0]
        
        for c in range(ord(cell1_c), ord(cell2_c)+1):
            for i in range(n, m+1):
                l.append(f"{chr(c)}{i}")
        
        return l