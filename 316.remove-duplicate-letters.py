#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {item: i for i, item in enumerate(s)}
        res = []
        for i, item in enumerate(s):
            if item not in res:
                while res and item < res[-1] and i < d[res[-1]]:
                    res.pop()
                res.append(item)
        return "".join(res)
        # last_occ = {}
        # res = []
        # visited = set()

        # for i in range(len(s)):
        #     last_occ[s[i]] = i

        # for i in range(len(s)):

        #     if s[i] not in visited:
        #         while (res and res[-1] > s[i] and last_occ[res[-1]] > i):
        #             visited.remove(res.pop())

        #         res.append(s[i])
        #         visited.add(s[i])

        # return ''.join(res)



# @lc code=end

