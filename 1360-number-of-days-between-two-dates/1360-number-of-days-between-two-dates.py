class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date11 = date1.split("-")
        date22 = date2.split("-")
        d0 = date(int(date11[0]), int(date11[1]), int(date11[2]))
        d1 = date(int(date22[0]), int(date22[1]), int(date22[2]))
        delta = d1 - d0
        return abs(delta.days)