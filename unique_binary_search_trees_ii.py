# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/unique-binary-search-trees-ii/
    """
    # @return a list of tree node
    def generateTrees(self, n):
        if n == 0:
            return [None]

        res = []
        for num in range(1, n+1):
            res.extend(self._gen(num, 1, n))
        return res

    def _gen(self, root, minval, maxval):
        res = []
        if root != minval:
            res1 = []
            for val in range(minval, root):
                res1.extend(self._gen(val, minval, root-1))
        else:
            res1 = [None] 
        if maxval != root:
            res2 = []
            for val in range(root+1, maxval+1):
                res2.extend(self._gen(val, root+1, maxval))
        else:
            res2 = [None]
        for left in res1:
            for right in res2:
                node = TreeNode(root)
                node.left = left
                node.right = right
                res.append(node)
        return res

if __name__ == "__main__":
    solution = Solution()
    from lib.tree import TreeNode
    nodes = solution.generateTrees(4)
    for node in nodes:
        print(node)
