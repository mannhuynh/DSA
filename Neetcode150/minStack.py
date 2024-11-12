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
