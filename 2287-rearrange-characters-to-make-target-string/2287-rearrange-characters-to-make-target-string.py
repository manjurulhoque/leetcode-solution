class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        words = Counter(s)
        n = 0
        b = False

        while True:
            for t in target:
                if t in words and words[t] > 0:
                    words[t] -= 1
                else:
                    b = True
                    break
            if b:
                break
            n += 1
        return n