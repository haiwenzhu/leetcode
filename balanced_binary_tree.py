# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    """
    @see https://oj.leetcode.com/problems/balanced-binary-tree/
    """
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        else:
            return abs(self._maxDeep(root.left) - self._maxDeep(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def _maxDeep(self, node):
        if node:
            if node.left and node.right:
                return max(self._maxDeep(node.left), self._maxDeep(node.right)) + 1
            elif node.left:
                return self._maxDeep(node.left) + 1
            elif node.right:
                return self._maxDeep(node.right) + 1
            else:
                return 1
        else:
            return 0
        
if __name__ == "__main__":
    from lib import tree
    parser = tree.TreeParser()
    solution = Solution()

    root = parser.parse([1,'#',2,'#',3])
    print(solution.isBalanced(root))
    root = parser.parse([1,2,2,3,3,3,3,4,4,4,4,4,4,'#','#',5,5])
    print(solution.isBalanced(root))
