class Solution {
public:
    vector<int> sortEvenOdd(vector<int>& nums) {
        vector<int> odd, even;
        vector<int> ans;
        
        for(int i = 0; i < size(nums); i++) {
            if(i % 2 == 0) {
                even.push_back(nums[i]);
            } else {
                odd.push_back(nums[i]);
            }
        }
        
        sort(even.begin(), even.end());
        sort(odd.begin(), odd.end(), greater<int>());
        
        int e = 0, o = 0;
        for(int i = 0; i < size(nums); i++) {
            if(i % 2 == 0) {
                ans.push_back(even[e++]);
            } else {
                ans.push_back(odd[o++]);
            }
        }
        return ans;
    }
};