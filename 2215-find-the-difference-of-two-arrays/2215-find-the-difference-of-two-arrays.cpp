class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<int> a1, a2;
        
        for(int i = 0; i < size(nums1); i++) {
            if(find(nums2.begin(), nums2.end(), nums1[i]) == nums2.end() && find(a1.begin(), a1.end(), nums1[i]) == a1.end()) {
                a1.push_back(nums1[i]);
            }
        }
        
        for(int i = 0; i < size(nums2); i++) {
            if(find(nums1.begin(), nums1.end(), nums2[i]) == nums1.end() && find(a2.begin(), a2.end(), nums2[i]) == a2.end()) {
                a2.push_back(nums2[i]);
            }
        }
        
        vector<vector<int>> ans;
        ans.push_back(a1);
        ans.push_back(a2);
        
        return ans;
    }
};