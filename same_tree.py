# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    """
    @see https://oj.leetcode.com/problems/same-tree/
    """
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        pq = collections.deque([p])
        qq = collections.deque([q])
        while pq and qq:
            pn = pq.popleft()
            qn = qq.popleft()
            if pn and qn:
                if pn.val != qn.val:
                    return False
                else:
                    pq.append(pn.left)
                    pq.append(pn.right)
                    qq.append(qn.left)
                    qq.append(qn.right)
            elif pn or qn:
                return False

        if pq or qq:
            return False
        else:
            return True

if __name__ == "__main__":
    from lib import tree 
    parser = tree.TreeParser()

    p = parser.parse([3,9,20,'#','#',15,7])
    q = parser.parse([3,9,20,'#','#',15,7])

    solution = Solution()
    print(solution.isSameTree(p, q))
    print(solution.isSameTree(None, None))
    
