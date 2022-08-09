class Solution {
public:
    #define ll long long
    #define MOD 1000000007
    int numFactoredBinaryTrees(vector<int>& arr) {
        ll ans =0;
        unordered_map<ll, ll> up;
        sort(arr.begin(), arr.end());
        for(int i=0; i< arr.size(); i++){
            ll currentans=1;
            for(int j=0; j< i; j++)
            {
                if(arr[i]% arr[j]) continue;
                int ans1= arr[i]/ arr[j];
                int ans2= arr[j];
                currentans= (currentans+ up[ans1]*up[ans2]%MOD)%MOD;
            }
            up[arr[i]]= currentans;
            ans = ans+ currentans;
        }
        return ans% MOD;
    }
};