class MyStack {
public:
    int _top;
    queue<int> p;
    queue<int> s;
        
    MyStack() {
    }
    
    void push(int x) {
        p.push(x);
        _top = x;
    }
    
    int pop() {
        while(p.size() != 1) {
            s.push(p.front());
            _top = p.front();
            p.pop();
        }
        int ele = p.front();
        p.pop();
        swap(p, s);
        return ele;
    }
    
    int top() {
        return _top;
    }
    
    bool empty() {
        return p.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */