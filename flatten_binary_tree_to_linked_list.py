# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
    """
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self._flatten(root)

    def _flatten(self, node):
        if node:
            left = node.left
            right = node.right
            tail = node
            if left:
                head,tmptail = self._flatten(left)
                tail.left = None
                tail.right = head
                tail = tmptail
            if right:
                head, tmptail = self._flatten(right)
                tail.left = None
                tail.right = head
                tail = tmptail
            return node, tail
        
if __name__ == "__main__":
    from lib import tree
    solution = Solution()
    parser = tree.TreeParser()
    root = parser.parse([1,2,3])
    solution.flatten(root)
    print(root)
