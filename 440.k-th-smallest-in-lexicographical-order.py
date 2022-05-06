#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # https://www.bilibili.com/video/BV1q5411A7fU?p=1
        cur = 1
        k -= 1
        while k>0:
            nodes = self.getNodes(n, cur)
            if nodes <= k:
                k -= nodes
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur 
    
    def getNodes(self, n, cur):
        totalNodes = 0
        while cur<=n:
            totalNodes += min(n-cur+1, 10)
            cur *= 10
        return totalNodes

            
        
# @lc code=end

