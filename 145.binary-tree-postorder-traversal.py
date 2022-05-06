#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        后续遍历二叉树，要求不使用递归。
        很明显需要使用栈来进行迭代。后续遍历是依序访问左子树，右子树，根节点。
        我们的入口是根节点，那么我们的栈应该先保存根，然后右子树，再保存左子树。

        分开来看，根的左孩子有可能是根而不是叶子结点，我们需要一路向下保存根节点，
        直到遇到叶子结点，才能保证根最先保存。

        怎么样保证右子树比左子树先保存呢？事实上我们访问的顺序是先左后右。现在我们只
        需要保证右子树比根节点优先输出（后入栈），而左子树已全部出栈就可以。怎么判断
        什么时候入栈（第一次遇到根（左孩子），第一次遇到右孩子），什么时候出栈（第二
        次遇到右孩子，第二次遇到根（左孩子））？我们需要有一个pre变量来记录之前遇到
        的最后一个节点。如果pre和当前节点的右孩子值相等，那么我们是第二次遇到根，此
        时右孩子早已访问，直接根出栈。否则，我们应访访问当前节点的右孩子（入栈）。
        """
        stack, cur, pre, res = [], root, None, []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                if stack[-1].right in (None, pre):
                    res.append(stack[-1].val)
                    pre = stack.pop()
                else:
                    cur = stack[-1].right
        return res
        

