#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
            
        ans = [[]]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                k = nums[i][j]
                if len(ans[-1]) < c:
                    ans[-1].append(k)
                else:
                    ans.append([k])
        return ans
# @lc code=end

