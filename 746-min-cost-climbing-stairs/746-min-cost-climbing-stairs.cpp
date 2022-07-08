class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int memo[1001]; memo[0] = 0; memo[1] = 0;
        
		for (int i = 2; i <= cost.size(); i++) 
            memo[i] = min(memo[i - 1] + cost[i - 1], memo[i - 2] + cost[i - 2]); 
		
        return memo[cost.size()]; 
    }
};