class Solution {
public:
    vector<int> diStringMatch(string s) {
        vector<int> r;
        int i = 0;
        int d = s.size();
        
        for(int j = 0; j < s.size(); j++) {
            if(s[j] == 'I') r.push_back(i++);
            else r.push_back(d--);
        }
        
        r.push_back(i++);
        
        return r;
    }
};