#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(n)
        """
        res, cnt = 0, 0
        d = {}
        for i, item in enumerate(nums):
            if item == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt == 0:
                res = i+1
            if cnt in d:
                res = max(res, i-d[cnt])
            else:
                d[cnt] = i 
        return res 
        

# @lc code=end

