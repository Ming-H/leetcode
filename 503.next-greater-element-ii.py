#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        遍历两轮数组
        """
        stack = []
        res = [-1]*len(nums)
        
        for i in list(range(len(nums)))*2:
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)            
        return res

        # nums.insert(0, nums[-1])
        # stack = []
        # dic = {}
        # for item in nums:
        #     while stack and item>stack[-1]:
        #         dic[stack.pop()] = item
        #     stack.append(item)
        # res = []
        # for item in nums[:-1]:
        #     res.append(dic[item])
        # return res

# @lc code=end

