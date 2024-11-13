"""Minimum Stack
Solved 
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O
(
1
)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = 0
        if self.min_stack:
            min_val = min(val, self.min_stack[-1])
        else:
            min_val = val
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

        
minStack = MinStack()
result = [
minStack.push(-2),
minStack.push(0),
minStack.push(-3),
minStack.getMin(),
minStack.pop(),
minStack.top(),
minStack.getMin()]

print(result)
