#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanDict ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        for i in range(len(s)):
            if s[i] == 'V' and s[i-1]=='I' and i!=0:
                ans = ans  - (2* romanDict[s[i-1]]) + romanDict[s[i]]
            elif s[i] == 'X' and s[i-1]=='I' and i!=0:
                ans = ans  - (2* romanDict[s[i-1]]) + romanDict[s[i]]
            elif s[i] == 'L' and s[i-1]=='X' and i!=0:
                ans = ans  - (2* romanDict[s[i-1]]) + romanDict[s[i]]
            elif s[i] == 'C' and s[i-1]=='X' and i!=0:
                ans = ans  - (2* romanDict[s[i-1]]) + romanDict[s[i]]
            elif s[i] == 'D' and s[i-1]=='C' and i!=0:
                ans = ans  - (2* romanDict[s[i-1]]) + romanDict[s[i]]
            elif s[i] == 'M' and s[i-1]=='C' and i!=0:
                ans = ans  - (2* romanDict[s[i-1]]) + romanDict[s[i]]
            else:
                ans= ans + romanDict[s[i]]
        
        return ans
        
# @lc code=end

