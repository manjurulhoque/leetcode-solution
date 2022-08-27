class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool m_i = true;
        bool m_d = true;
        
        for(int i = 0; i < size(nums) - 1; i++) {
            if(nums[i] <= nums[i + 1]) {
                m_i = true;
            } else {
                m_i = false;
                break;
            }
        }
        
        for(int i = 0; i < size(nums) - 1; i++) {
            if(nums[i] >= nums[i + 1]) {
                m_d = true;
            } else {
                m_d = false;
                break;
            }
        }
        
        if(m_i) return true;
        if(m_d) return true;
        
        return false;
    }
};