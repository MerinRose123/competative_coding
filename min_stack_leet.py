"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""
"""
Explanation

https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = 0
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_val = val
            self.stack.append(val)
        elif val <= self.min_val :
            self.stack.append(2*val - self.min_val)
            self.min_val = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val < self.min_val:
            result = self.min_val
            self.min_val = 2 * self.min_val - val
            val = result
        return val

    def top(self) -> int:
        return self.stack[-1] if self.stack[-1] >= self.min_val else self.min_val

    def getMin(self) -> int:
        return self.min_val
