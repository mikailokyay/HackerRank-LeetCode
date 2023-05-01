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

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        valid_dic = {"(": ")", "{": "}", "[": "]"}

        if not s or len(s) < 2:
            return False

        stack = []
        for p in s:
            if p in valid_dic.keys():
                stack.append(p)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if p == ')' and last != '(':
                    return False
                if p == ']' and last != '[':
                    return False
                if p == '}' and last != '{':
                    return False
        return not stack
