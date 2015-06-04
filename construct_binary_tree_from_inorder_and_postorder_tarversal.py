# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
    """
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self._build(inorder, 0, len(inorder), postorder, 0, len(postorder))

    def _build(self, inorder, i, j, postorder, i1, j1):
        if i < j:
            node = TreeNode(postorder[j1-1])
            pos = inorder.index(node.val)
            node.left = self._build(inorder, i, pos, postorder, i1, i1+pos-i)
            node.right = self._build(inorder, pos+1, j, postorder, i1+pos-i, j1-1)
            return node
        else:
            return None

if __name__ == "__main__":
    from lib.tree import TreeNode
    solution = Solution()
    print(solution.buildTree([2,1,3],[2,3,1]))
