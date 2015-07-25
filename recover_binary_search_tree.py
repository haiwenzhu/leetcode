# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @see https://leetcode.com/problems/recover-binary-search-tree/
    """
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        """
        order the nodes first, the first and last node which violate the order is what we want find
        """
        self.nodes = []
        if root:
            self.innerOrder(root)
        l = len(self.nodes)
        node1 = None #node1 is the largest node of the warp nodes
        node2 = None #node2 is the smallest node of the swap nodes
        if l > 1:
            if self.nodes[0].val > self.nodes[1].val:
                node1 = self.nodes[0]
            if not node1 or not node2:
                for i in range(1, l-1):
                    if self.nodes[i].val > self.nodes[i-1].val and self.nodes[i].val > self.nodes[i+1].val and not node1:
                        node1 = self.nodes[i]
                    if self.nodes[i].val < self.nodes[i-1].val and self.nodes[i].val < self.nodes[i+1].val:
                        node2 = self.nodes[i]
            #the smallest node must be the last node
            if self.nodes[l-1].val < self.nodes[l-2].val:
                node2 = self.nodes[l-1]

            if node1 and node2:
                val = node1.val
                node1.val = node2.val
                node2.val = val

    def innerOrder(self, node):
        if node.left:
            self.innerOrder(node.left)
        self.nodes.append(node)
        if node.right:
            self.innerOrder(node.right)

if __name__ == "__main__":
    from lib import tree
    parser = tree.TreeParser()
    solution = Solution()
    root = parser.parse([2,4,'#',3,'#',5,'#',1])
    solution.recoverTree(root)
    print(root)
