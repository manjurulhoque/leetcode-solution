class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(int i = 0; i < size(matrix); i++) {
            for(int j = 0; j < size(matrix[i]); j++) {
                if(matrix[i][j] == target) return true;
            }
        }
        
        return false;
    }
};