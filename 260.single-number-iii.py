#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        https://blog.csdn.net/coder_orz/article/details/52071599
        使用异或，如果对所有nums里面的数都使用异或，最后的结果就是
        我们要求的数异或的结果，因为其他重复的值异或的结果变成0了。
        然后查看这两个数异或的结果，如果一些字节异或的结果为1，则表
        明这两个数在那个位置不同。
        然后把所有数字分成两组，一组是在对应位置为1的，另一组在对应
        位置不为1。两个不同的数字就是我们要找的。

        """
        diff = 0
        for item in nums:
            diff ^= item
        diff &= -diff
        res = [0, 0]
        for item in nums:
            if item & diff:
                res[0] ^= item
            else:
                res[1] ^= item
        return res



        
  

# @lc code=end

