class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        mx = 0
        l = len(number)
        for i in range(l):
            if number[i] == digit:
                tmp = number
                tmp1 = tmp[:i] + '' + tmp[i+1:]
                tmp2 = "".join(tmp1)
                mx = max(mx, int(tmp2))
        return str(mx)