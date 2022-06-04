class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict()
        for path in paths:
            d.update({path[0]: path[1]})
        
        for path in paths:
            if not d.get(path[1]):
                return path[1]
        