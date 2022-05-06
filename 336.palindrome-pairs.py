#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:
    def palindromePairs(self, words):
        # 结果数组
        result = []
        # 字典，用于获取索引
        worddict = {word: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            count = len(word)
            for j in range(count + 1):
                # 获取字段的前半部分，后半部分
                prefix, subfix = word[:j], word[j:]
                # 前半部分的反转，后半部分的反转
                reprefix, resubfix = prefix[::-1], subfix[::-1]
                # 如果前半部分是 palindrome 并且后半部分的反转在字典中
                if prefix == reprefix and resubfix in worddict:
                    m = worddict[resubfix]
                    # 不能取到字符本身
                    if m != i: 
                        result.append([m, i]) # 添加的顺序要与可组成回文串的顺序对应
                # 如果后半部分是回文字符串，并且前半部分的逆序在字典中
                if j != count and subfix == resubfix and reprefix in worddict:
                    result.append([i, worddict[reprefix]])
                    
        return result

# @lc code=end

