#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict ={}
        
        for idx,num in enumerate(nums):
            diff = target - num
            if diff in numsDict:
                ans = [idx,numsDict[diff]] 
            numsDict[num] = idx
        return ans
# @lc code=end

