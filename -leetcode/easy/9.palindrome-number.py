#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        numStr = str(x)
        palindrome=numStr[::-1]

        if numStr == palindrome:
            return True
        else:
            return False
# @lc code=end

