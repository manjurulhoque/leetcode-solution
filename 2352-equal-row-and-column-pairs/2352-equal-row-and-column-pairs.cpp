class Solution {
public:
    int equalPairs(vector<vector<int>>& a) {
        int n = a.size();
        int c = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                bool is = true;
                for(int k = 0; k < n; k++) {
                    if(a[i][k] != a[k][j]) {
                        is = false;
                    }
                }
                if(is) c += 1;
            }
        }
        return c;
    }
};