class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int, int> pairs;
        int c = 0;
        
        for(int i = 0; i < nums.size(); i++) pairs[nums[i]]++;
        
        for(auto x : pairs) {
            c += x.second / 2;
        }
        return c == nums.size() / 2;
    }
};