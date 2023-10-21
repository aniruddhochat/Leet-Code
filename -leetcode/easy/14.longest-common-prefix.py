#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cnt=0
        shortestWord = min(strs,key=len)
        for i in range(len(shortestWord)):
            cnt = 0
            for string in strs:
                if shortestWord == string[0:len(shortestWord)]:
                    cnt+=1
            if cnt != len(strs):
                shortestWord = shortestWord[:-1]
        return shortestWord
        
# @lc code=end

