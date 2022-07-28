class Solution {
public:
    bool isValid(string str) {
        int hypen = 0, n = str.length();
        for(int i = 0; i < n; i++) {
            if(str[i] == '-') hypen++;
            else if(str[i] >= '0' && str[i] <= '9') return false;
            else if((str[i] == '.' || str[i] == '!' || str[i] == ',') && (i != n - 1)) return false;
            if(hypen >= 2) return false;
            if(i == 0 || i == n - 1) {
                if(str[i] == '-') return false;
            }
            else {
                if(str[i] == '-') {
                    if(!(str[i - 1] <= 'z' && str[i + 1] >= 'a')) return false;
                }
            }
        }
        return true;
    }
    int countValidWords(string sentence) {
        int res = 0; string str = "";
        for(int i = 0; i < sentence.length(); i++) {
            if(sentence[i] == ' ') {
                if(str.length() && isValid(str)) res++;
                str = "";
            } else str.push_back(sentence[i]);
        }
        if(str.length() && isValid(str)) res++;
        return res;
    }
};