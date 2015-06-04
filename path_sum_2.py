# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    """
    @see https://oj.leetcode.com/problems/path-sum-ii/
    """
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]] if root.val == sum else []
        else:
            res = []
            q = collections.deque([root])
            s = root.val
            item = [root.val]
            while q:
                node = q.pop()
                if node:
                    s -= node.val
                    item.pop()
                    if node.left:
                        #node is not leaf
                        if node.left.left or node.left.right:
                            q.append(node)
                            q.append(node.left)
                            s = s + node.val + node.left.val
                            item.append(node.val)
                            item.append(node.left.val)
                            node.left = None
                        else:
                            if s + node.val + node.left.val == sum:
                                tmp = list(item)
                                tmp.extend([node.val, node.left.val])
                                res.append(tmp)
                            if node.right:
                                node.left = None
                                s += node.val
                                item.append(node.val)
                                q.append(node)
                    elif node.right:
                        #node.right is not leaf
                        if node.right.left or node.right.right:
                            q.append(node)
                            q.append(node.right)
                            s = s + node.val + node.right.val
                            item.append(node.val)
                            item.append(node.right.val)
                            node.right = None
                        else:
                            if s + node.val + node.right.val == sum:
                                tmp = list(item)
                                tmp.extend([node.val, node.right.val])
                                res.append(tmp)
            return res

if __name__ == "__main__":
    from lib import tree
    parser = tree.TreeParser()
    solution = Solution()
    root = parser.parse([1, 2, 2])
    print(solution.pathSum(root, 3))
    print(solution.pathSum(root, 2))
    print(solution.pathSum(None, 0))

