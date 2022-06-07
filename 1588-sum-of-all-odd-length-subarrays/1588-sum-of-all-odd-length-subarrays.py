class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subs = []
        count = 0
        for n in range(1,len(arr)+1,2):
            for i in range(len(arr)+1-n):
                count += sum(arr[i:i+n])
    
        return count