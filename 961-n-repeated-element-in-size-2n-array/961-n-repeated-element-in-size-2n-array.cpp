class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int l = size(nums);
        map<int, int> mp;
        
        for(int i = 0; i < l; i++) mp[nums[i]]++;
        
        for(auto m : mp) {
            if(m.second * 2 == l) return m.first;
        }
        
        return 0;
    }
};