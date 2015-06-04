# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    """
    @see https://oj.leetcode.com/problems/path-sum/
    """
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        elif not root.left and not root.right:
            return sum == root.val
        else:
            q = collections.deque([root])
            s = root.val if root else 0
            while q:
                node = q.pop()
                if node:
                    s -= node.val
                    if node.left:
                        #node is not leaf
                        if node.left.left or node.left.right:
                            q.append(node)
                            q.append(node.left)
                            s = s + node.val + node.left.val
                            node.left = None
                        else:
                            if s + node.val + node.left.val == sum:
                                return True
                            if node.right:
                                node.left = None
                                s += node.val
                                q.append(node)
                    elif node.right:
                        #node.right is not leaf
                        if node.right.left or node.right.right:
                            q.append(node)
                            q.append(node.right)
                            s = s + node.val + node.right.val
                            node.right = None
                        else:
                            if s + node.val + node.right.val == sum:
                                return True
            return False

if __name__ == "__main__":
    from lib import tree
    parser = tree.TreeParser()
    solution = Solution()
    root = parser.parse([1, 2, 3])
    print(solution.hasPathSum(root, 3))
    print(solution.hasPathSum(root, 2))
    print(solution.hasPathSum(None, 0))

