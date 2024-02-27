#implement stack using queue costly pop
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
        #push data to queue1 
        self.q1.append(data)

    # pop from stack is O(n)
    def pop(self):
        # check queue1 empty 
        if not self.q1:
            # return None
            return None 
        # if queue1 has more than one element
        while len(self.q1) !=1:
            #pop and append to queue2
            self.q2.append(self.q1.popleft())
        # now queue1 has last element 
        x = self.q1.popleft()
        # now swap queue
        self.q1, self.q2 = self.q2, self.q1
        return x
    def top(self):
        if not self.q1:
            return None
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        x = self.q1[0]
        self.q1, self.q2 = self.q2, self.q1
        return x
    def size(self):
        return len(self.q1)
if __name__ == "__main__":
    stk = Stack()
    stk.push(5)
    stk.push(8)
    stk.push(18)
    print(stk.size())
    stk.push(20)
    stk.push(28)
    print(stk.pop())
    stk.push(81)
    print(stk.top())