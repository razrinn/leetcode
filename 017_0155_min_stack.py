class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack == []:
            self.min_stack.append(val)
        else:
            min_val = self.min_stack[-1]
            if val <= min_val:
                self.min_stack.append(val)


    def pop(self) -> None:
        popped = self.stack.pop()
        if self.min_stack[-1] == popped:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()