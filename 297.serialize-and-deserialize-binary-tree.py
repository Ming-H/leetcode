#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        res = []
        def preOrder(root):
            if not root:
                res.append('#')
            else:
                res.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(res)

    def deserialize(self, data):
        nums = [val for val in data.split()]
        def build():
            if nums:
                val = nums.pop(0)
                if val == '#':
                    return None
                else:
                    root = TreeNode(int(val))
                    root.left = build()
                    root.right = build()
            return root
        return build()
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

