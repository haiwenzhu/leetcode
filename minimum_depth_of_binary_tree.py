# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    """
    @see https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
    """
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        else:
            q = collections.deque([(root, 1)])
            while q:
                item = q.popleft()
                node = item[0]
                if node.left or node.right:
                    if node.left:
                        q.append((node.left, item[1]+1))
                    if node.right:
                        q.append((node.right, item[1]+1))
                else:
                    return item[1]

if __name__  == "__main__":
    from lib import tree
    parser = tree.TreeParser()
    solution = Solution()
    root = parser.parse([1,2,3, 4, 5])
    print(solution.minDepth(root))
    
