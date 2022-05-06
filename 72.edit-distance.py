#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        比较的两个字符 word1[i] 和 word2[j]，若二者相同，一切好说，
        直接跳到下一个位置。若不相同，有三种处理方法，首先是直接插入一
        个 word2[j]，那么 word2[j] 位置的字符就跳过了，接着比较 
        word1[i] 和 word2[j+1] 即可。第二个种方法是删除，即将 word1[i] 
        字符直接删掉，接着比较 word1[i+1] 和 word2[j] 即可。第三种则是
        将 word1[i] 修改为 word2[j]，接着比较 word1[i+1] 和 word[j+1]
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        #边界
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[m][n]


        # len1 = len(word1)
        # len2 = len(word2)
        # if len1 == 0:
        #     return len2
        # if len2 == 0:
        #     return len1
        # num = [[0 for i in range(len2+1)] for j in range(len1+1)]

        # for j in range(len2+1):
        #     num[0][j] = j

        # for i in range(len1+1):
        #     num[i][0] = i

        # if word1[0] != word2[0]:
        #     num[1][1] = 1

        # if len1 >= 1 and len2 >= 1:
        #     for i in range(1, len1+1):
        #         for j in range(1, len2+1):
        #             num[i][j] = min(num[i - 1][j] + 1,
        #                             num[i][j - 1] + 1, 
        #                             num[i - 1][j - 1] + int(word1[i-1] != word2[j-1]))

        # return num[len1][len2] 

        # l1, l2 = len(word1)+1, len(word2)+1
        # pre = [i for i in range(l2)]
        
        # for i in range(1, l1):
        #     cur = [i]*l2
        #     for j in range(1, l2):
        #         cur[j] = min(cur[j-1]+1, pre[j]+1,  \
        #             pre[j-1]+(word1[i-1]!=word2[j-1]))
        #     pre = cur[:]
        # return pre[-1]

