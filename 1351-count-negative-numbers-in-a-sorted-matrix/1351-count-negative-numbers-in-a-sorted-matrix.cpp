class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int c = 0;
        
        for(int i = 0; i < size(grid); i++) {
            for(int j = 0; j < size(grid[i]); j++) {
                if(grid[i][j] < 0) c++;
            }
        }
        
        return c;
    }
};