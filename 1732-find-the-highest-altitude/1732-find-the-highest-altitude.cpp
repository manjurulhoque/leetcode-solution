class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> res;
        res.push_back(0);
        
        for(int i = 0; i < gain.size(); i++) {
            res.push_back(res[i] + gain[i]);
        }
        
        return *max_element(res.begin(), res.end());
    }
};