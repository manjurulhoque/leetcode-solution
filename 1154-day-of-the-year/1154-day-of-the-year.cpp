class Solution {
public:
    int dayOfYear(string date) {
        vector<int> days{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int y = stoi(date.substr(0, 4)), m = stoi(date.substr(5, 2)), d = stoi(date.substr(8, 2));
        if (m > 2 && y % 4 == 0 && (y % 100 != 0 || y % 400 == 0)) ++d;
        while (--m) d += days[m - 1];
        return d;
    }
};