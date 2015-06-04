# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    """
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        node = head
        lastVal = None
        lastNode = None
        while node:
            if (node.next and node.val == node.next.val) or \
               node.val == lastVal:
                if lastNode:
                    lastNode.next = node.next
                else:
                    head = node.next
            else:
                lastNode = node
            lastVal = node.val
            node = node.next
        return head

if __name__ == "__main__":
    solution = Solution()
    from lib import list
    l = list.List([1,1,1])
    print(solution.deleteDuplicates(l.head))
