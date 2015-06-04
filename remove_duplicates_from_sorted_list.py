# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
    """
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        node = head
        while node:
            if node.next and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

if __name__ == "__main__":
    solution = Solution()
    from lib import list
    l = list.List([1,1,2,3,3])
    print(solution.deleteDuplicates(l.head))

