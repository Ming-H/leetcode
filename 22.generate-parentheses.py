#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # """
        # """
        # if n == 0: 
        #     return ['']
        # ans = []
        # for c in range(n):
        #     for left in self.generateParenthesis(c):
        #         for right in self.generateParenthesis(n-1-c):
        #             ans.append('({}){}'.format(left, right))
        # return ans
        '''
        回溯。不是先生成所有组合，而是用递归回溯的方法生成所有合法的组合。
        '''
        def generate(A = '', left = 0, right = 0):
            if len(A) == 2 * n:
                res.append("".join(A))
                return
            if left < n:  #先对左括号递归
                generate(A + '(', left + 1, right)
            if right < left:  #再对右括号递归
                generate(A + ')', left, right+1)
        res = []
        generate()
        return res
        # ————————————————
        # 版权声明：本文为CSDN博主「caisense」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
        # 原文链接：https://blog.csdn.net/u012033124/article/details/80532460

