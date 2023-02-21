#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        https://www.cnblogs.com/grandyang/p/5705750.html
        这里需要一个一维数组 dp，其中 dp[i] 表示目标数为i的解的个数，
        然后从1遍历到 target，对于每一个数i，遍历 nums 数组，
        如果 i>=x, dp[i] += dp[i - x]。这个也很好理解，比如说对于 
        [1,2,3] 4，这个例子，当计算 dp[3] 的时候，3可以拆分为 1+x，
        而x即为 dp[2]，3也可以拆分为 2+x，此时x为 dp[1]，3同样可以
        拆为 3+x，此时x为 dp[0]，把所有的情况加起来就是组成3的所有情况
        """
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for item in nums:
                if i >= item:
                    dp[i] += dp[i-item]
        return dp[-1]











# @lc code=end

