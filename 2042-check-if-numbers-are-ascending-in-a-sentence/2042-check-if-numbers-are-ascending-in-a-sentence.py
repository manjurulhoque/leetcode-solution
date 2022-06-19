class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(" ")
        nums = list()
        for word in words:
            if word.isnumeric():
                word = int(word)
                nums.append(word)
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                continue
            else:
                return False
        return True