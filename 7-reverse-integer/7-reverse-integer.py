class Solution:
    def reverse(self, x: int) -> int:
        # https://stackoverflow.com/q/11928669/5559590
        if x < 0:
            res = int("-" + str(x)[:0:-1]) 
        else:
            res = int(str(x)[::-1])
        return( res if abs(res) <= 0x7FFFFFFF else 0) 
        