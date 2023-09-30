## Stack -- LIFO
## Queue -- FIFO

class MyStack:
    def __init__(self):
        self.dq1 = deque()

    def push(self, x: int) -> None:
        self.dq1.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.dq1) - 1):
            self.push(self.dq1.popleft())
        
        return self.dq1.popleft()

    def top(self) -> int:
        return self.dq1[-1]
        
    def empty(self) -> bool:
        return len(self.dq1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()