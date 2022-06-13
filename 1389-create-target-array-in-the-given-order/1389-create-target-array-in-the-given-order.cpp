class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> arr;
        arr.reserve(nums.size());
        
        for(int i = 0; i < nums.size(); i++) {
            auto itPos = arr.begin() + index[i];
            arr.insert(itPos, nums[i]);
        }
        
        return arr;
    }
};