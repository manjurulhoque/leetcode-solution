class Solution:
    def isUniqueChars(self, st):
        # Initialize occurrences of all characters
        char_set = [False] * 128
        # For every character, check if it exists
        # in char_set
        for i in range(len(st)):
            # Find ASCII value and check if it
            # exists in set.
            val = ord(st[i])
            if char_set[val]:
                return False

            char_set[val] = True

        return True
 

    def countGoodSubstrings(self, test_str: str) -> int:
        res = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1) if len(test_str[i:j]) == 3]
        c = 0
        for r in res:
            if self.isUniqueChars(r):
                c += 1
        return c
