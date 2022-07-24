class Solution {
public:
    char repeatedCharacter(string s) {
        int f[256];
        memset(f, 0, sizeof f);
        for(char c : s) {
            f[c]++;
            if(f[c] > 1) return c;
        }
        return ' ';
    }
};