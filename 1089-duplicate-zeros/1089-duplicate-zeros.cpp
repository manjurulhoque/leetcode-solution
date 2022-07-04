class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int l = arr.size();
        vector<int> res;
        
        for(int i = 0; i < l; i++) {
            if(arr[i] == 0) {
                //res.push_back(arr[i]);
                //res.push_back(0);
                auto itPos = arr.begin() + i + 1;
                auto newIt = arr.insert(itPos, 0);
                i++;
            } else {
                //res.push_back(arr[i]);
            }
            //res.push_back(arr[i]);
        }
        for(int i = 0; i < l; i++) res.push_back(arr[i]);
        arr = res;
    }
};