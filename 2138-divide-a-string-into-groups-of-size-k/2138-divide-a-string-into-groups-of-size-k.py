class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr = []
        l = len(s)
        
        n = 0
        ss = ""
        for i, c in enumerate(list(s)):
            if n < k:
                ss += c
                n += 1
                
                if n == k and (i + 1) % k == 0:
                    arr.append(ss)
                    n = 0
                    ss = ""
                elif l - i + 1 in [1, 2]:
                    arr.append(ss)
                    n = 0
                    ss = ""
        
        if len(arr[-1]) < k:
            arr[-1] += fill * (k - len(arr[-1]))
        return arr