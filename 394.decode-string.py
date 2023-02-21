#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        stack = []; cnt = 0; curStr = ''
        for item in s:
            if item == '[':
                stack.append(curStr)
                stack.append(cnt)
                curStr = ''
                cnt = 0
            elif item == ']':
                num = stack.pop()
                tmp = stack.pop()
                curStr = tmp + num*curStr
            elif item.isdigit():     
                cnt = cnt*10 + int(item)
            else:
                curStr += item
        return curStr



# @lc code=end

