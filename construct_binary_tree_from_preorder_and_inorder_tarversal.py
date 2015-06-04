# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    """
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self._build(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def _build(self, preorder, i, j, inorder, i1, j1):
        if i < j:
            node = TreeNode(preorder[i])
            pos = inorder.index(node.val)
            node.left = self._build(preorder, i+1, i+pos+1-i1, inorder, i1, pos)
            node.right = self._build(preorder, i+pos+1-i1, j, inorder, pos+1, j1)
            return node
        else:
            return None

if __name__ == "__main__":
    from lib.tree import TreeNode
    solution = Solution()
    print(solution.buildTree([1,2,3],[2,1,3]))
