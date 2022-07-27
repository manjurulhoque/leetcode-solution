class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        int c = 0;
        bool found = false;
        
        for(int i = 0; i < size(words1); i++) {
            for(int j = 0; j < size(words1); j++) {
                if(i != j && words1[i] == words1[j]) {
                    found = true;
                    break;
                }
            }
            
            int n = 0;
            if(!found) {
                for(int j = 0; j < size(words2); j++) {
                    if(words1[i] == words2[j]) {
                        n++;
                    }
                }
                
                if(n == 1) c += n;
            }
            found = false;
        }
        
        return c;
    }
};