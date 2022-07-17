class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        
        for(int i = 0; i < size(arr); i++) {
            for(int j = 0; j < size(arr); j++) {
                if(i != j && arr[i] == 2 * arr[j]) return true;
            }
        }
        
        return false;
    }
};