# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -math.inf
        def DFS(node):
            if not node:
                return -math.inf
            
            result = node.val    
            
            left = DFS(node.left)
            if left > 0:
                result += left

            right = DFS(node.right)
            if right > 0:
                result += right

            self.ans = max(self.ans, result)## max not always contain root
            
            addOn = max(right, left)

            return node.val + addOn if addOn > 0 else node.val

        DFS(root)

        return self.ans
        