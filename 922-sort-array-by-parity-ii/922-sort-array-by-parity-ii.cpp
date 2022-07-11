class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        stack<int> odd, even;
        
        for(auto a : nums) {
            if(a % 2 == 0) even.push(a);
            else odd.push(a);
        }
        vector<int> ans;
        
        for(int i = 0; i < size(nums); i++) {
            if(i % 2 == 0) {
                ans.push_back(even.top());
                even.pop();
            } else {
                ans.push_back(odd.top());
                odd.pop();
            }
        }
        
        return ans;
    }
};