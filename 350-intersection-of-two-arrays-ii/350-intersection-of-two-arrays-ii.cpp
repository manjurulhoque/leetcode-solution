class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        
        map<int, int> mp1, mp2;
        
        for(int i = 0; i < size(nums1); i++) mp1[nums1[i]]++;
        
        for(int i = 0; i < size(nums2); i++) mp2[nums2[i]]++;
        
        for(auto a : mp1) {
            for(auto b : mp2) {
                if(a.first == b.first) {
                    for(int k = 0; k < min(a.second, b.second); k++) {
                        ans.push_back(a.first);
                    }
                }
            }
        }
        
        return ans;
    }
};