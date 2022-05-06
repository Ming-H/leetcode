#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp=[]
        ops=("/","+","*","-")
        for i in iter(tokens):
            if i not in ops:
                temp.append(i)
            else:
                b,a=map(int, (temp.pop(),temp.pop()))
                if i=="+":
                    temp.append(a+b)
                elif i=="-":
                    temp.append(a-b)
                elif i=="*":
                    temp.append(a*b)
                else:
                    temp.append(a/b)
        return int(temp[0])

# @lc code=end

