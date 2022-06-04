class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        ln = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        fh, sh = 0, 0
        for i in range(0, int(ln/2)):
            if s[i] in vowels:
                fh += 1
        for i in range(int(ln/2), ln):
            if s[i] in vowels:
                sh += 1
        return fh == sh
        