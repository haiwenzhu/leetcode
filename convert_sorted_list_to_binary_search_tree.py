# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from lib.tree import TreeNode 

class Solution:
    """
    @see https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
    """
    # @param num, a list of integers
    # @return a tree node
    def sortedListToBST(self, head):
        num = []
        while head:
            num.append(head.val)
            head = head.next
        return self.sortedArrayToBST(num)

    def sortedArrayToBST(self, num):
        n = len(num)
        if n == 0:
            return None
        else:
            i = n // 2
            node = TreeNode(num[i])
            node.left = self.sortedArrayToBST(num[0:i])
            node.right = self.sortedArrayToBST(num[i+1:])
            return node

if __name__ == "__main__":
    from lib import list
    l = list.List([1,2,3,4])
    solution = Solution()
    print(solution.sortedListToBST(l.head))
