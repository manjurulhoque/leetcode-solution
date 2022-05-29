class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        ss = sentence.split(" ")
        words = []
        for s in ss:
            if s[0] == '$':
                remain = s[1:]
                if not remain.isnumeric():
                    words.append(s)
                    continue
                total = int(s[1:])
                n = (total*discount)/100
                total -= n
                total = "$%.2f" % total
                words.append(total)
            else:
                words.append(s)
        
        return " ".join(words)