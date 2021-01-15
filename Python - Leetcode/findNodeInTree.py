#Find a Corresponding Node of a Binary Tree in a Clone of That Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchTarget(self, tree: TreeNode, val: int) -> TreeNode: 
        if tree is None:
            return None
        elif tree.val == val: 
            return tree
        else:
            leftNode = self.searchTarget(tree.left,val)
            rightNode = self.searchTarget(tree.right,val)
            if leftNode:
                return leftNode
            else:
                return rightNode
            
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        val = target.val 
        return self.searchTarget(cloned, val)