#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        A = [int(item) for item in list(str(num))]
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if d in last and last[d]>i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num
        
# @lc code=end

