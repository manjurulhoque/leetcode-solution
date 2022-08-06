class Solution {
public:
    int secondHighest(string s) {
        set<int> ss;
        for(auto c : s) {
            int n = c - '0';
            if(n >= 0 && n <= 9) {
                ss.insert(n);
            }
        }
        //for(auto a : ss) cout<<a<<endl;
        //cout<<s[1]<<endl;
        if(size(ss) > 1) {
            auto my_vect = std::vector(ss.begin(), ss.end());
            return my_vect[size(my_vect) - 2];
        }
        return -1;
    }
};