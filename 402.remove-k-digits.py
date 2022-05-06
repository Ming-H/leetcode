#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def remove_leading_zero(self, num):
        i = 0
        while i < len(num) and num[i] == '0':
            i += 1
        if i == len(num):
            return '0'
        return num[i:]

    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'

        if k == 0:
            return self.remove_leading_zero(num)
    
        to_remove_index = 0
        while to_remove_index < len(num)-1 and num[to_remove_index] <= num[to_remove_index + 1]:
            to_remove_index += 1

        return self.removeKdigits(num[:to_remove_index] + num[to_remove_index+1:], k-1)
	
# @lc code=end

