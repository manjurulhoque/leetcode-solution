class Solution:
    def countTriples(self, n: int) -> int:
#         c = 0
        
#         for i in range(1, n + 1):
#             for j in range(1, n + 1):
#                 for k in range(1, n + 1):
#                     if i * i + j * j == k * k:
#                         c += 1
        
#         return c
        out = 0
        for i in range(1,n+1):
            for j in range(i+1, n+1):
                a = i**2 + j **2
                if sqrt(a).is_integer() and sqrt(a) <= n:
                    out += 1 * 2
                a = 0
        return out