#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        def dfs(i):
            if i <= n:
                result.append(i)
                for d in range(10):
                    dfs(10 * i + d)
        result = []
        for i in range(1, 10):
            dfs(i)
        return result





     