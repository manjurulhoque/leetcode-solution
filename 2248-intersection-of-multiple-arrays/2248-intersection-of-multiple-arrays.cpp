class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        vector<int> ans;
        
        int n=nums.size();
        for(auto x: nums[0])
        {
            bool flag=0;
            for(int i=1;i<n;i++)
            {
                if(find(nums[i].begin(),nums[i].end(),x)==nums[i].end())
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
                ans.push_back(x);
        }
        sort(ans.begin(),ans.end());
        return ans;
    }
};