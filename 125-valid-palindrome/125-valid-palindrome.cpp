class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        string res = "";
        string res1;
        
        for(int i = 0; i < s.size(); i++) {
            if((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= '0' && s[i] <= '9')) {
                res += s[i];
            }
        }
        //cout << res;
        res1 = res;
        reverse(res1.begin(), res1.end());
        return res == res1;
    }
};