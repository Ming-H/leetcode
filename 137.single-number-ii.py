#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        https://www.cnblogs.com/grandyang/p/4263927.html
        """
        # a,b=0,0
        # for num in nums:
        #     b=b^num&~a
        #     a=a^num&~b
        # return b
        """
        用3个整数来表示 INT 的各位的出现次数情况，one 表示出现了1次，
        two 表示出现了2次。当出现3次的时候该位清零。最后答案就是one的值。
        ones   代表第 ith 位只出现一次的掩码变量
        twos  代表第 ith 位只出现两次次的掩码变量
        threes  代表第 ith 位只出现三次的掩码变量
        假设现在有一个数字1，更新 one 的方法就是 ‘亦或’ 这个1，则 one 
        就变成了1，而 two 的更新方法是用上一个状态下的 one 去 ‘与’ 上
        数字1，然后 ‘或’ 上这个结果，这样假如之前 one 是1，那么此时 two 
        也会变成1，这 make sense，因为说明是当前位遇到两个1了；反之如果之
        前 one 是0，那么现在 two 也就是0。注意更新的顺序是先更新 two，
        再更新 one，不理解的话只要带个只有一个数字1的输入数组看一下就不难
        理解了。然后更新 three，如果此时 one 和 two 都是1了，由于先更新的
         two，再更新的 one，two 为1，说明此时至少有两个数字1了，而此时 one 
         为1，说明了此时已经有了三个数字1，这块要仔细想清楚，因为 one 是要 
         ‘亦或’ 一个1的，值能为1，说明之前 one 为0，实际情况是，当第二个1
         来的时候，two 先更新为1，此时 one 再更新为0，下面 three 就是0了，
         那么 ‘与’ 上t hree 的相反数1不会改变 one 和 two 的值；那么当第三
         个1来的时候，two 还是1，此时 one 就更新为1了，那么 three 就更新为
         1了，此时就要清空 one 和 two 了，让它们 ‘与’ 上 three 的相反数0即
         可，最终结果将会保存在 one 中
        """
        one = 0
        two = 0
        three = 0
        for i in range(len(nums)):
            two |= one & nums[i]
            one ^= nums[i]
            three = one & two
            one &= ~three
            two &= ~three
        return one
# @lc code=end

