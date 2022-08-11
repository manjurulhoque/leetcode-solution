class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int, int> mp;
        vector<int> result;

        for(int i=0; i<arr1.size(); i++)
            mp[arr1[i]]++;

        for(int i=0; i<arr2.size(); i++){
            while(mp[arr2[i]]>0){
                result.push_back(arr2[i]);
                mp[arr2[i]]--;
            }
        }

        for(auto it : mp){
            while(it.second>0){
                result.push_back(it.first);
                (it.second)--;
            }   
        }

        return result;
        
        
    }
};