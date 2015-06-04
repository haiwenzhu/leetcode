# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/merge-two-sorted-lists/
    """
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        h1, h2 = l1, l2
        if h1 and h2:
            if h1.val < h2.val:
                head = h1
                h1 = h1.next
            else:
                head = h2
                h2 = h2.next
        elif h1:
            head = h1
            h1 = h1.next
        elif h2:
            head = h2
            h2 = h2.next
        else:
            head = None
        h = head
        while h1 and h2:
            if h1.val < h2.val:
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next
            h = h.next
        if h:
            if h1:
                h.next = h1
            else:
                h.next = h2
        return head
        
if __name__ == "__main__":
    solution = Solution()
    import lib.list
    l1 = lib.list.List([])
    l2 = lib.list.List([])
    print(solution.mergeTwoLists(l1.head, l2.head))
