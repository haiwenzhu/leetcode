# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
    """
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

if __name__ == "__main__":
    from lib import tree
    parser = tree.TreeParser()
    solution = Solution()
    root = parser.parse([1,2,3,'#','#',4])
    print(solution.maxDepth(root))
    print(solution.maxDepth(None))
        

