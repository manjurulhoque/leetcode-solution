class MyQueue {
public:
    stack<int> s1; //Main stack for doing operation
    stack<int> s2; //Auxiliary stack needed for some operation 
    MyQueue() {
        
    }
    
    void push(int x) {
        // In a queue the last inserted element is popped out last. So to this for a stack we need to push it to the bottom of the stack. 
        while(!s1.empty()){  
            s2.push(s1.top());
            s1.pop();
        }
        s1.push(x);
        while(!s2.empty()){
            s1.push(s2.top());
            s2.pop();
        }
    }
    
    int pop() {
        //Main stack is s1 so store and remove top, then return it. 
        int y = s1.top();
        s1.pop();
        return y;
    }
    
    int peek() {
        return s1.top();
    }
    
    bool empty() {
        return s1.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */