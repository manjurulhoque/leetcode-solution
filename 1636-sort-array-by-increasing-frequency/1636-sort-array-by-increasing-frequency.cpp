class Solution {
public:
    static bool comp(pair<int,int>p,pair<int,int>q)
      //first column stores frequency i.e duplicates and second column stores value
    {//if the duplicates are equal then we will return by greater value first...
      if(p.first==q.first)
      {
        return p.second>q.second;
      }
      ///else we will return as per frequency.
    return p.first<q.first;
    }
        vector<int> frequencySort(vector<int>& nums) {
            
        map<int,int>sk; 
        for(int i=0;i<nums.size();i++){ ///inserting value and its duplicate in map...
            sk[nums[i]]++;   
        }
        vector<int>ans;
        vector<pair<int,int>>temp; //creating pair so that we can sort
        for(auto i:sk){
            temp.push_back({i.second,i.first});  ///now adding duplicate in first and value in second column...
        }
        sort(temp.begin(),temp.end(),comp); ///sorting by function...
        for(auto z:temp){
            int a=z.first;
            int b=z.second;
            for(int j=0;j<a;j++){
                ans.push_back(b);
            }
        }
        
        return ans;
    }
};