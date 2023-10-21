#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        strStack=[]
        parathesis = {'(':')','{':'}','[':']'}
        for string in s:
            if string == '(' or string == '{' or string == '[':
                strStack.append(string)
            elif string == ')' or string == '}' or string == ']':
                if not strStack:
                    return False
                currentString = strStack.pop()
                if parathesis[currentString]!=string:
                    return False
        if not strStack:
            return True
            
            
# @lc code=end

