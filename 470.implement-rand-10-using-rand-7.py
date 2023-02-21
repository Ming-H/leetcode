#
# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # acceptable is the desired range which can generate required integer directly
        curr = acceptable = 7 * 7 - (7 * 7) % 10
        # if current no is not in the acceptable range, discard it and repeat the process again
        while curr >= acceptable:
            curr = (rand7() - 1) * 7 + rand7() - 1
        return curr % 10 + 1



# @lc code=end

