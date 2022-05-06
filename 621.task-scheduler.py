#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # https://www.cnblogs.com/George1994/p/7396673.html
        output = [0]*26
        for item in tasks:
            output[ord(item)-ord('A')] += 1
        max_o = max(output) # 计算最大任务个数
        count = 0 # 获取有几个任务能够被安排到最后
        for item in output:
            if item==max_o:
                count += 1
        return max(len(tasks), (max_o-1)*(n+1)+count)
        
        # @lc code=end

