#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, s: str, p: str) -> int:
        '''
        https://www.cnblogs.com/grandyang/p/6992403.html
        KMP的整体时间复杂度为O(m + n)。
        若存在字串返回字串在字符串中开始的位置下标，或者返回-1

        失配时，模式串向右移动的距离 = 已匹配字符数 - 失配字符的上一位字符所对应的最大长度值
        失配时，模式串向右移动的距离 = 失配字符所在位置 - 失配字符对应的next值。
        '''
        pnext = self.gen_pnext(p)
        i, j = 0, 0
        while (i < len(s) and j < len(p)) :
            if (j == - 1 or s[i] == p[j]) : 
                i += 1
                j += 1
            else:
                j = pnext[j] #pnext包含-1， 致使j=-1
        return i-j if j==len(p) else -1

    def gen_pnext(self, p):
        k, j = -1, 0
        pnext = [-1 for i in range(len(p))]
        while j < len(p) - 1:
            if (k == -1 or p[j] == p[k]):
                k += 1
                j += 1
                pnext[j] = k if p[j] != p[k] else pnext[k] 
                # 如果p[j] == p[next[j]]了，再用p[next[j]]和s[i]去匹配必然会失配
            
            else:
                k = pnext[k]
        return pnext


    #     pnext = self.gen_pnext(needle)
    #     n = len(haystack)
    #     m = len(needle)
    #     i, j = 0, 0
    #     while (i<n) and (j<m):
    #         if (haystack[i]==needle[j]):
    #             i += 1
    #             j += 1
    #         elif (j!=0):
    #             j = pnext[j-1] # 前一位的pnext数组的值
    #         else:
    #             i += 1
    #     if (j == m):
    #         return i-j
    #     else:
    #         return -1
            
    # def gen_pnext(self, substring):
    #     """
    #     构造临时数组pnext
    #     """
    #     index, m = 0, len(substring)
    #     pnext = [0]*m
    #     i = 1
    #     while i < m:
    #         if (substring[i] == substring[index]):
    #             pnext[i] = index + 1
    #             index += 1
    #             i += 1
    #         elif (index!=0):
    #             index = pnext[index-1]
    #         else:
    #             pnext[i] = 0
    #             i += 1
    #     return pnext

    
