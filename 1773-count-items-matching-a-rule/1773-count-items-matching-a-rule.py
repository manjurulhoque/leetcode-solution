class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        var = 0
        if ruleKey=="color":
            var = 1
        elif ruleKey=="name":
            var = 2    
        for item in items:
            if item[var] == ruleValue:
                count += 1
        return count