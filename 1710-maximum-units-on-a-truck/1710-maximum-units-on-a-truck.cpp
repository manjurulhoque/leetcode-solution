class Solution {
public:
    static bool sortcol(const vector<int>& v1, const vector<int>& v2)
    {
        return v1[1] > v2[1];
    }
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        int ans = 0;
        
        sort(boxTypes.begin(), boxTypes.end(), sortcol);
        
        for(auto b : boxTypes){
            if (b[0] <= truckSize){ 
                truckSize -= b[0];
                ans += (b[1] * b[0]);
                if(truckSize == 0)
                    return ans;
                }
            else{
                ans += truckSize * b[1];
                return ans;
            }
        }
        
        return ans;
    }
};