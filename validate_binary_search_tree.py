# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self._valid(root, -2**31 - 1, 2**31)
        
    def _valid(self, root, minval, maxval):
        if root and (root.val < minval or root.val > maxval):
            return False
        if root:
            return self._valid(root.left, minval, root.val-1) and \
                    self._valid(root.right, root.val+1, maxval)
        else:
            return True

if __name__ == "__main__":
    solution = Solution()
    from lib import tree
    root = tree.TreeParser().parse([1,'#',2,'#',3])
    print(solution.isValidBST(root))
