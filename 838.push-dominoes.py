#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Time and Space Complexity: O(N)
        """
        # symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        # symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        # res = list(dominoes)
        # for (i, x), (j, y) in zip(symbols, symbols[1:]):
        #     if x == y:
        #         for k in range(i+1, j):
        #             res[k] = x
        #     elif x > y: #RL
        #         for k in range(i+1, j):
        #             if k-i < j-k:
        #                 res[k] = 'R'
        #             elif k-i == j-k:
        #                 res[k] = '.'
        #             else:
        #                 res[k] = 'L'
        # return "".join(res)

        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R': 
                f = N
            elif dominoes[i] == 'L': 
                f = 0
            else: 
                f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L': 
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else: 
                f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f==0 else 'R' if f > 0 else 'L'
                       for f in force)


# @lc code=end

