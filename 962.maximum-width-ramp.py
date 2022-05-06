#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        #return reduce(lambda x, y: (max(x[0], y[1] - x[1]), min(y[1], x[1])), 
        #    sorted([(val, i) for i, val in enumerate(A)]), (0, len(A) + 1))[0]
        import bisect
        N = len(A)
        ans = 0
        candidates = [(A[N-1], N-1)]
        # candidates: i's decreasing, by increasing value of A[i]
        for i in range(N-2, -1, -1):
            # Find largest j in candidates with A[j] >= A[i]
            jx = bisect.bisect(candidates, (A[i],))
            if jx < len(candidates):
                ans = max(ans, candidates[jx][1] - i)
            else:
                candidates.append((A[i], i))

        return ans
# @lc code=end

    