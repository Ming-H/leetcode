#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        https://www.cnblogs.com/chruny/p/5478262.html
        """
        # if len(s) == 0:
        #     return ""
        # ans = []
        # begin = i = 0
        # mark = True
        # while i < len(s):
        #     if s[i] != ' ' and mark:
        #         begin = i
        #         mark = False
        #     if s[i] == ' ' and i > 0 and s[i - 1] != ' ':
        #         ans.append(s[begin:i])
        #         while i < len(s) and s[i] == ' ':
        #             i += 1
        #         begin = i
        #     i += 1

        # if s[-1] != ' ':
        #     ans.append(s[begin:len(s)])
        
        # j = len(ans)
        # if j == 0:
        #     return ""
        # res = ans[j - 1]
        # j -= 1
        # while j > 0:
        #     res += ' ' + ans[j - 1]
        #     j -= 1
        # return res
        return ' '.join([item for item in s.strip().split(' ') if len(item)>0][::-1])



