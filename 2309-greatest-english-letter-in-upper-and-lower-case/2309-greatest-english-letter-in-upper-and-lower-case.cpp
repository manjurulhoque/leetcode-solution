class Solution {
public:
    string greatestLetter(string s) {
        vector<int> v1(26,0),v2(26,0);
        string ans ="";
        for(auto &x:s)
        {
            if(x>='a'&&x<='z')
            {
                v1[x-'a']++;
            }
            else        
            {
                v2[x-'A']++;
            }
        }
        for(int i = 25;i >= 0;i--)
        {
            if(v1[i] && v2[i])
            {
                return ans += (i + 'A');
            }
        }
        return ans;
    }
};