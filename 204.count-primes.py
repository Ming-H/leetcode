#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        从2开始遍历到根号n，先找到第一个质数2，然后将其所有的
        倍数全部标记出来，然后到下一个质数3，标记其所有倍数，
        一次类推，直到根号n，此时数组中未被标记的数字就是质数。
        """
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, n):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = False
        return sum(dp)




        
# @lc code=end

