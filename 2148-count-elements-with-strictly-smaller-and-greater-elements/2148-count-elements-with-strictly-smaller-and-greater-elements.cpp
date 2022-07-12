class Solution {
public:
    int countElements(vector<int>& nums) {
        //if(size(nums) == 2) return 0;
        int n = size(nums);
        
        // brute force
        sort(nums.begin(), nums.end());
        int c = 0;
        // 2, 7, 11, 15
        int min = nums[0];
        int max = nums[n - 1];
        for(int i = 0; i < n; i++) {
            if(nums[i] > min && nums[i] < max) c++;
        }
        
        return c;
    }
};