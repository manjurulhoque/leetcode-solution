class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        l = []
        if n % 2 == 0:
            for i in range(1, int(n / 2) + 1):
                l.append(i)
                l.append(i * -1)
        else:
            for i in range(1, int(n / 2) + 1):
                l.append(i)
                l.append(i * -1)
            l.append(0)
        return l