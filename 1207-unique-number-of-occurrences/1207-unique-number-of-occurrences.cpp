class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int, int> mp;
        
        for(int i = 0; i < size(arr); i++) mp[arr[i]]++;
        
        vector<int> a;
        set<int> s;
        
        for(auto m : mp) {
            a.push_back(m.second);
            s.insert(m.second);
        }
        
        return size(a) == size(s);
    }
};