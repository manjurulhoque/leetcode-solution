class Solution {
public:
    int countAsterisks(string s) {
        short int numofasteriks = 0;
        bool found = false;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '*' && !found )numofasteriks++;

            if (s[i] == '|' && !found)
                found = true;
            else if (s[i] == '|' && found) 
                found = false;
        }

        return numofasteriks;
    }
};