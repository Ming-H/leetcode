#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        https://www.cnblogs.com/lightwindy/p/8674041.html
        解法1: 桶排序Bucket Sort， Time: O(n), Space: O(n)
        1. 遍历数组nums，利用Hash map统计每个数字出现的次数。
        2. 遍历map，初始化一个行数为len(nums) + 1的二维数组，
            将出现次数为i ( i∈[1, n] )的所有数字加到第i行。
        3. 逆序遍历二维数组(从频率高的开始)，将其中的前k行的元素输出。
        """
        n = len(nums)
        cntDict = collections.defaultdict(int)
        for item in nums:
            cntDict[item] += 1
        freqList = [[] for i in range(n + 1)]
        for p in cntDict:
            freqList[cntDict[p]].append(p)
        ans = []
        for p in range(n, 0, -1):
            ans += freqList[p]
        return ans[:k]
