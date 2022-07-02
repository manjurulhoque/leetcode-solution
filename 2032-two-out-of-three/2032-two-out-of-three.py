class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = nums1 + nums2 + nums3
        ans = []
        # print(nums2)
        
        for i in range(len(res)):
            if (res[i] in nums1 and res[i] in nums2) or (res[i] in nums2 and res[i] in nums3) or (res[i] in nums1 and res[i] in nums3):
                ans.append(res[i])
        
        return list(set(ans))