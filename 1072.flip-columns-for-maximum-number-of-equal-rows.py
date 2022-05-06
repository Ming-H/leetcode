#
# @lc app=leetcode id=1072 lang=python3
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#

# @lc code=start
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        import collections
        cache = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            cache[str(vals)] += 1
            cache[str(trans)] += 1
        return max(cache.values())






# @lc code=end

