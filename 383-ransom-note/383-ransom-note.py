class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notes = dict()
        magazines = dict()
        for c in ransomNote:
            if c not in notes:
                notes[c] = 1
            else:
                notes[c] += 1
        
        for c in magazine:
            if c not in magazines:
                magazines[c] = 1
            else:
                magazines[c] += 1
                
        for c in ransomNote:
            if c not in magazines or magazines[c] < notes[c]:
                return False
        
        return True