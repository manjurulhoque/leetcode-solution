class Solution:
    def fib(self, n: int) -> int:
        # n1, n2 = 0, 1
        # count = 0
        # while count < n:
        #     #print(n1)
        #     nth = n1 + n2
        #     n1 = n2
        #     n2 = nth
        #     count += 1
        # return n1
        if n < 2:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)