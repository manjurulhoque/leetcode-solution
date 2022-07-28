class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        
        //vector<int> ss(s.begin(), s.end());
        int val = 1;
        for(auto i : s) {
            cout<<i<<endl;
            if(i> 0) {
                if(i != val) return val;
                else val++;
            }
        }
        
        return val;
    }
};