class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int c = 0;
        
        for(int i = 0; i < size(nums); i++) {
            for(int j = 0; j < size(nums); j++) {
                for(int k = 0; k < size(nums); k++) {
                    if(i < j < k) {
                        if(nums[j] - nums[i] == diff && nums[k] - nums[j] == diff) c++;
                    }
                }
            }
        }
        
        return c;
    }
};