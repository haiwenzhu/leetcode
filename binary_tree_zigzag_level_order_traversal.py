# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    """
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        res = []
        curLevel = [root] if root else []
        curVals = []
        nextLevel = []
        level = 1
        while curLevel or nextLevel:
            if not curLevel:
                res.append(curVals[0:])
                curVals = []
                curLevel = nextLevel[0:]
                nextLevel = []
                level += 1
            node = curLevel.pop(0)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            if level % 2 == 1:
                curVals.append(node.val)
            else:
                curVals[0:0] = [node.val]
        if curVals:
            res.append(curVals)
        return res

if __name__ == "__main__":
    solution = Solution()
    from lib import tree
    root = tree.TreeParser().parse([3,9,20,'#','#',15,7])
    print(solution.zigzagLevelOrder(None))
