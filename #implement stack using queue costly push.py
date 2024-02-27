#implement stack using queue costly push
# import library
from collections import deque
# create stack class
class Stack:
    # initiate two queue
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    # push to stack costly
    def push(self, data):
        #push data to queue2 
        self.q2.append(data)
        # pop from queue1 and append to queue2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # swap queue1 with queue2 so always queue2 will be empty to push
        self.q1, self.q2 = self.q2, self.q1
    # pop from stack is O(1)
    def pop(self):
        # always pop from queue1
        if self.q1:
            return self.q1.popleft()
        return "Empty Stack"
    def top(self):
        if self.q1:
            return self.q1[0]
        return None
    def size(self):
        return len(self.q1)
if __name__ == "__main__":
    stk = Stack()
    stk.push(5)
    stk.push(8)
    print(stk.size())
    stk.push(20)
    print(stk.pop())