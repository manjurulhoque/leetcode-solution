class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int c = 0, l = size(strs);
        
        for(int i = 0; i < strs[0].size(); i++) {
            for(int j = 1; j < l; j++) {
                //cout<<('c' > 'd')<<endl;
                //cout<<strs[j][i]<<endl;
                if(strs[j][i] < strs[j - 1][i]) {
                    c++;
                    break;
                }
            }
            //cout<<endl;
        }
        
        return c;
    }
};