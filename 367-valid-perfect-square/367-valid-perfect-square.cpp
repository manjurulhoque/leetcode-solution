class Solution {
public:
    bool isPerfectSquare(int num) {
        long l = 1;
        long r = (num / 2) + 1;
        
        while(l <= r) {
            long mid = (l + r) / 2;
            long long ans = mid * mid;
            if(ans == num) return true;
            if(ans > num) r = mid - 1;
            else l = mid + 1;
        }

        return false;
    }
};