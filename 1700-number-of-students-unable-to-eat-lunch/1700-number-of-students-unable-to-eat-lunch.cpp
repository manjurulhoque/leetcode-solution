class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        queue<int> remainingStudents;
        stack<int> stackSandwich;
        for(int i=0; i<students.size(); i++){
            remainingStudents.push(students[i]);
        }
        for(int i=students.size()-1; i >= 0; i--){
            stackSandwich.push(sandwiches[i]);
        }
        
        int count = 0;
        while(!remainingStudents.empty()){
            if(stackSandwich.top() ==  remainingStudents.front()){
                stackSandwich.pop();
                remainingStudents.pop();
                count = 0;
            }
            else{
                int temp = remainingStudents.front();
                remainingStudents.push(temp);
                remainingStudents.pop();
                count++;
            }
            if(count == remainingStudents.size())
                return remainingStudents.size();
        }
        return 0;
    }
};