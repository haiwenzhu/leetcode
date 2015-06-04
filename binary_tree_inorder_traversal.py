# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/binary-tree-inorder-traversal/
    """
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res = []
        if root:
            res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
        return res
       
if __name__ == "__main__":
    solution = Solution()
    from lib import tree
    parser = tree.TreeParser()
    root = parser.parse([1,'#',2,3])
    print(solution.inorderTraversal(root))
