class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hashmap = {}
        for i in range(lowLimit, highLimit +1):
            digit_sum = 0
            while i:
                digit_sum += i%10
                i = i//10
            # if digit_sum not in hashmap:
            #     hashmap[digit_sum] = 1
            # else:
            #     hashmap[digit_sum] += 1
            hashmap[digit_sum] = hashmap.get(digit_sum, 0) + 1
        return max(hashmap.values())