#
# @lc app=leetcode id=522 lang=python3
#
# [522] Longest Uncommon Subsequence II
#

# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        d = collections.Counter(strs)
        L = sorted(d.keys(), key = len, reverse = True)
        for i, item in enumerate(L):
            if d[item] != 1: 
                continue
            Flag = True
            # 判断item是不是最长非公共子序列
            for j in range(i):
                index, flag = -1, True
                for alpha in item:
                    index = L[j].find(alpha,index+1)
                    if index == -1:
                        flag = False
                        break
                if flag: # item 是重复的子序列，不满足
                    Flag = False
                    break
            # 如果是最长非公共子序列
            if Flag: 
                return len(item)
        return -1
# @lc code=end

