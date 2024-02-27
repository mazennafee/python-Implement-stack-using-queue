#implement stack using one queue 
# import library
from collections import deque
# create stack class
class Stack:
    # initiate queue
    def __init__(self):
        self.q = deque()
    # push
    def push(self, data):
        # get last size 
        prev_size = len(self.q)
        # append new data
        self.q.append(data)
        # create loop to pop previous elements
        for i in range(prev_size):
            self.q.append(self.q.popleft())
    # pop
    def pop(self):
        if not self.q:
            return None
        return self.q.popleft()
    # top
    def top(self):
        if not self.q:
            return None
        return self.q[0]
    # size
    def size(self):
        return len(self.q)
if __name__ == "__main__":
    stk = Stack()
    stk.push(5)
    stk.push(8)
    stk.push(18)
    print(stk.size())
    stk.push(20)
    print(stk.top())
    stk.push(28)
    print(stk.pop())
    stk.push(81)
    print(stk.top())