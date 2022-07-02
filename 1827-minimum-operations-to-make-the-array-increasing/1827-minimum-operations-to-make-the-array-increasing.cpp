class Solution {
public:
    int minOperations(vector<int>& nums) {
        int c = 0;
        
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i] <= nums[i - 1]) {
                int change = nums[i - 1] - nums[i] + 1;
                c += change;
                nums[i] += change;
            }
        }
        
        return c;
    }
};