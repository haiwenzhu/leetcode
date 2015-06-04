# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from lib.tree import TreeNode 

class Solution:
    """
    @see https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
    """
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        n = len(num)
        if n == 0:
            return None
        else:
            i = n // 2
            node = TreeNode(num[i])
            node.left = self.sortedArrayToBST(num[0:i])
            node.right = self.sortedArrayToBST(num[i+1:])
            return node

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedArrayToBST([1,2,3,4]))
