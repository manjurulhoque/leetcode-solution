class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c = 0
        for item in items:
            if ruleKey == "type" and item[0] == ruleValue:
                c += 1
            elif ruleKey == "color" and item[1] == ruleValue:
                c += 1
            elif ruleKey == "name" and item[2] == ruleValue:
                c += 1
        return c