#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        R, C = len(M), len(M[0])
        res = [[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                cnt = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0<=nr<R and 0<=nc<C:
                            res[r][c] += M[nr][nc]
                            cnt += 1
                res[r][c] /= cnt 
                res[r][c] = int(res[r][c])
        return res 





# @lc code=end

