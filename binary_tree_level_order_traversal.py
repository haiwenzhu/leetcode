import collections
class Solution:
    """
    @see https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
    """
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        levels = {} 
        queue = collections.deque([(root, 0)])
        while queue:
            item = queue.popleft()
            if item[0] != None:
                if item[1] not in levels:
                    levels[item[1]] = []
                levels[item[1]].append(item[0].val)

                if item[0].left != None:
                    queue.append((item[0].left, item[1]+1))
                if item[0].right != None:
                    queue.append((item[0].right, item[1]+1))
        
        return list(levels.itervalues())

if __name__ == "__main__":
    from lib import tree
    parser = tree.TreeParser()
    root = parser.parse([3,9,20,'#','#',15,7])
    solution = Solution()
    print(solution.levelOrder(root))
    print(solution.levelOrder(None))
