class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        # print(seats)
        
        n = 0
        for i in range(len(seats)):
            n += abs(students[i] - seats[i])
        
        return n