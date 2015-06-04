# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    """
    @see https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
    """
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root:
            q = collections.deque([(root, 1)])
            preLevel = 1
            lists = []
            item = []
            while q:
                node = q.popleft()
                if node[1] != preLevel:
                    lists.append(item)
                    item = []
                    preLevel = node[1]
                item.append(node[0].val)
                
                if node[0].left:
                    q.append((node[0].left, node[1]+1))
                if node[0].right:
                    q.append((node[0].right, node[1]+1))
            lists.append(item)
            lists.reverse()
            return lists
        else:
            return []

if __name__ == "__main__":
    solution = Solution()
    from lib import tree
    parser = tree.TreeParser()
    root = parser.parse([3,9,20,'#','#',15,7])
    print(solution.levelOrderBottom(root))
    print(solution.levelOrderBottom(None))
