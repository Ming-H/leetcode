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
        https://www.cnblogs.com/grandyang/p/6529857.html
        """
        # 为了当 sum 第一次出现0的时候，即这个子数组是从原数组的起始
        # 位置开始，需要计算这个子数组的长度，而不是建立当前子数组之
        # 和 sum 和其结束位置之间的映射
        d = {0:-1} 
        maxlen, count = 0, 0
        for i in range(len(nums)):
            count = count+1 if nums[i]==1 else count-1
            if count in d:
                maxlen = max(maxlen, i-d[count])
            else:
                d[count] = i
        return maxlen

        

# @lc code=end

