#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s)
        sorted_chars = sorted(
            counter.items(), key=lambda x: x[1], reverse=True)
        return ''.join(char*freq for char, freq in sorted_chars)


# @lc code=end
