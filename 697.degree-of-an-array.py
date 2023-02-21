#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        left, right, cnt = {},{},{}
        for i, item in enumerate(nums):
            if item not in left:
                left[item] = i
            right[item] = i 
            cnt[item] = cnt.get(item, 0) + 1
        res = len(nums)
        degree = max(cnt.values())
        for x in cnt:
            if cnt[x] == degree:
                res = min(res, right[x]-left[x]+1)
        return res 






# @lc code=end

