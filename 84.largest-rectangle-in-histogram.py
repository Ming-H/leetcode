#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        The stack maintain the indexes of buildings with ascending height.
        Before adding a new building, pop the building who is taller than 
        the new one. The building popped out represent the height of a 
        rectangle with the new building as the right boundary and the 
        current stack top as the left boundary. Calculate its area and 
        update ans of maximum area. Boundary is handled using dummy buildings.
        
        https://www.cnblogs.com/grandyang/p/4322653.html
        维护一个栈，用来保存递增序列，相当于上面那种方法的找局部峰值。
        我们可以看到，直方图矩形面积要最大的话，需要尽可能的使得连续的矩形多，
        并且最低一块的高度要高。有点像木桶原理一样，总是最低的那块板子决定桶的装水量。
        因此我们需要一个递增栈，当遇到大的数字直接进栈，而当遇到小于栈顶元素的数字时，
        就要取出栈顶元素进行处理了，那取出的顺序就是从高板子到矮板子了，于是乎遇到的
        较小的数字只是一个触发，表示现在需要开始计算矩形面积了，为了使得最后一块板
        子也被处理，这里用了个小 trick，在高度数组最后面加上一个0，这样原先的最后
        一个板子也可以被处理了。由于栈顶元素是矩形的高度，那么关键就是求出来宽度，
        那么跟之前那道 Trapping Rain Water 一样，单调栈中不能放高度，而是需要放坐标。
        由于我们先取出栈中最高的板子，那么就可以先算出长度为1的矩形面积了，然后再取
        下一个板子，此时根据矮板子的高度算长度为2的矩形面积，以此类推，知道数字大于
        栈顶元素为止，再次进栈
        
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]: 
                # 当前元素小于上一个元素
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        # heights.pop()
        return ans
            

