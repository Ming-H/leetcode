#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rindex = {item:i for i, item in enumerate(s)}
        res = ''
        for i, item in enumerate(s):
            if item not in res:
                while item<res[-1:] and i<rindex[res[-1:]]:
                    res = res[:-1] 
                res += item 
        return res 
        # last_occ = {}
        # stack = []
        # visited = set()

        # for i in range(len(s)):
        #     last_occ[s[i]] = i

        # for i in range(len(s)):

        #     if s[i] not in visited:
        #         while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
        #             visited.remove(stack.pop())

        #         stack.append(s[i])
        #         visited.add(s[i])

        # return ''.join(stack)



# @lc code=end

