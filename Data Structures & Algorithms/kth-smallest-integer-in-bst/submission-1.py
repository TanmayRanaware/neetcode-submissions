# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=0
        self.ans=0
        self.inorder(root, k)
        return self.ans
    def inorder(self, node, k):
        if not node:
            return 
            
        self.inorder(node.left, k)
        self.count+=1
        if self.count==k:
            self.ans=node.val
            return
        self.inorder(node.right, k)

                