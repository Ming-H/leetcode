#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preOrder(root):
            if root:
                res.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nums = [item for item in data.split()]
        def build(nums, lower_bound, upper_bound):
            if nums and lower_bound < int(nums[0]) < upper_bound:
                root_value = int(nums.pop(0))
                root_node = TreeNode(root_value)
                root_node.left = build(nums, lower_bound, root_value )
                root_node.right = build(nums, root_value, upper_bound )
                return root_node        
        return build(nums, float('-inf'), float('inf')) 




# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

