#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []
	# Push element x to the back of queue...
    def push(self, x):
        self.in_stk.append(x)
	# Remove the element from the front of the queue and returns it...
    def pop(self):
        self.peek()
        return self.out_stk.pop()
	# Get the front element...
    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]
	# Return whether the queue is empty...
    def empty(self):
        return not self.in_stk and not self.out_stk
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
