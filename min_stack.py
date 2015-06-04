class MinStack:
    """ 
    # @see https://oj.leetcode.com/problems/min-stack/
    """
    def __init__(self):
        self.stack = []
        self.mini = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)             

        if self.mini == None or x < self.mini:
            self.mini = x

        return x
    
    # @return nothing
    def pop(self):
        top = self.stack.pop()
        if top == self.mini:
            self.mini = min(self.stack) if len(self.stack) > 0 else None
    
    # @return an integer
    def top(self):
        return self.stack[-1]                              
    
    # @return an integer
    def getMin(self):
        return self.mini

if __name__ == "__main__":
    stack = MinStack()
    print(stack.push(2))
    print(stack.push(1))
    print(stack.push(3))
    print(stack.top())
    stack.pop()
    print(stack.getMin())
    stack.pop()
    stack.pop()
    print(stack.getMin())
    stack.push(-3)
    print(stack.getMin())
