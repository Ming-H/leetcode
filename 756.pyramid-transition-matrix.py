#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#

# @lc code=start
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        #Comments can be used to cache intermediate results
        #seen = set()
        def solve(A):
            if len(A) == 1: return True
            #if A in seen: return False
            #seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i = 0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)
# @lc code=end

