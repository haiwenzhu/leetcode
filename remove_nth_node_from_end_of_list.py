# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
    """
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        if n == len(nodes):
            return head.next
        else:
            nodes[-n-1].next = nodes[-n].next
            return head
           
if __name__ == "__main__":
    from lib import list
    solution  = Solution()

    l = list.List([1,2,3,4,5])
    head = solution.removeNthFromEnd(l.head, 2)
    print(head)
    head = solution.removeNthFromEnd(head, 4)
    print(head)
