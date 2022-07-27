class Solution {
public:
    string removeDuplicates(string s) {
//         jump:
//         int l = s.size();
//         for(int i = 0; i < l; i++) {
//             cout<<i<<endl;
//             if(i < l && s[i] == s[i + 1]) {
//                 s.replace(i, i + 1, "");
//                 goto jump;
//             }
//         }
        
//         return s;
        int i = 0;
        while(i <= s.length()){
            if(s[i + 1] == s[i]){
                s.erase(i, 2);
                if(i > 0) i--;
            }
            else i++;
        }
        return s;
    }
};