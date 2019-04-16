# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxValue = -100
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath(root)
        return self.maxValue
    
    def maxPath(self, cur):
        leftMax = 0
        if cur.left:
            leftMax = max(0, self.maxPath(cur.left))
        rightMax = 0
        if cur.right:
            rightMax = max(0, self.maxPath(cur.right))
        self.maxValue = max(self.maxValue, rightMax + leftMax + cur.val)
        return max(rightMax, leftMax) + cur.val
        