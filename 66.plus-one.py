#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits):
        # num = 0
        # for i in range(len(digits)):
        #     num += digits[i] * pow(10, (len(digits)-1-i))
        # return [int(i) for i in str(num+1)]

        res = []
        val = 0
        for i, item in enumerate(digits[::-1]):
            if i == 0:
                val, item = divmod(item + val + 1, 10)
            else:
                val, item = divmod(item + val, 10)
            res.append(item)
        if val:
            res.append(val)
        return res[::-1]











