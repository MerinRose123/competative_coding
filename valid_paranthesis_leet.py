"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
"""
Explanation
Put all opening paranthesis to stack. When a closing paranthesis appear if the corresponding opening paranthesis is not in stack top then it is not valid.
"""
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pair_dict = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for elem in s:
            if elem in pair_dict.keys():
                stack.append(elem)
            else:
                if len(stack) == 0:
                    return False
                match = stack.pop()
                if pair_dict[match] != elem:
                    return False
        if len(stack) == 0:
            return True
        return False
    
