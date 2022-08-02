class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> mp;
        
        for(int i = 0; i < size(arr); i++) mp[arr[i]]++;
        
        // vector<string> ans;
        
        for(auto s : arr) {
            if(mp[s] == 1) {
                k--;
            }
            if(k == 0) return s;
        }
        
        return "";
    }
};