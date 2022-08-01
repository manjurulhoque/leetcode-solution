class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        map<int, int> mp;
        
        for(int i = 0; i < size(nums); i++) mp[nums[i]]++;
        
        int c = 0;
        vector<int> a;
        a.push_back(0);
        
        for(auto m : mp) {
            c += m.second / 2;
            if(m.second % 2 != 0) a[0] += 1;
            // else a.push_back(0);
        }
        
        //if(size(a) == 0) a.push_back(0);
        
        a.insert(a.begin(), c);
        
        return a;
    }
};