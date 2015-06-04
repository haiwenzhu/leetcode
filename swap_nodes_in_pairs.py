# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/swap-nodes-in-pairs/
    """
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        h = head
        while h and h.next:
            val = h.next.val
            h.next.val = h.val
            h.val = val
            h = h.next.next
        return head

if __name__ == "__main__":
    from lib import list
    solution = Solution()
    l = list.List([1,2,3,4])
    print(solution.swapPairs(l.head))


