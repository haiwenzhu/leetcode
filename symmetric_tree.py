# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    """
    @see https://oj.leetcode.com/problems/symmetric-tree/
    """
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        q = collections.deque([(root, 0)]) 
        vals = []
        last_deep = 0
        while q:
            item = q.popleft()
            node = item[0]
            deep = item[1]

            if deep != last_deep: 
                if not self._cmpList(vals, last_deep):
                    return False
                vals = []

            if node:
                q.append((node.left, deep+1))
                q.append((node.right, deep+1))
                vals.append(node.val)
            else:
                vals.append('#')
            last_deep = deep;

        return self._cmpList(vals, last_deep)            


    def _cmpList(self, vals, deep):
        length = len(vals)
        tmpvals = list(vals)
        tmpvals.reverse()
        if vals != tmpvals:
            return False
        else:
            return True


if __name__ == "__main__":
    from lib import tree
    parser = tree.TreeParser()

    root = parser.parse([-64,12,18,-4,-53,'#',76,'#',-51,'#','#',-93,3,'#',-31,47,'#',3,53,-81,33,4,'#',-51,-44,-60,11,'#','#','#','#',78,'#',-35,-64,26,-81,-31,27,60,74,'#','#',8,-38,47,12,-24,'#',-59,-49,-11,-51,67,'#','#','#','#','#','#','#',-67,'#',-37,-19,10,-55,72,'#','#','#',-70,17,-4,'#','#','#','#','#','#','#',3,80,44,-88,-91,'#',48,-90,-30,'#','#',90,-34,37,'#','#',73,-38,-31,-85,-31,-96,'#','#',-18,67,34,72,'#',-17,-77,'#',56,-65,-88,-53,'#','#','#',-33,86,'#',81,-42,'#','#',98,-40,70,-26,24,'#','#','#','#',92,72,-27,'#','#','#','#','#','#',-67,'#','#','#','#','#','#','#',-54,-66,-36,'#',-72,'#','#',43,'#','#','#',-92,-1,-98,'#','#','#','#','#','#','#',39,-84,'#','#','#','#','#','#','#','#','#','#','#','#','#',-93,'#','#','#',98])
    
    solution = Solution()
    print(solution.isSymmetric(root))
    #print(solution.isSymmetric(None))
