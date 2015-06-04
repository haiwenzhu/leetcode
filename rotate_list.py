# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/rotate-list/
    """
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        h = head
        length = 1
        while h and h.next:
            length += 1
            h = h.next
        tail = h
        h = head
        k %= length
        if k > 0:
            for i in range(0, length-k-1):
                h = h.next
            tail.next = head
            head = h.next
            h.next = None
        return head

if __name__ == "__main__":
    solution = Solution()
    from lib import list
    l = list.List([])
    print(solution.rotateRight(l.head, 0))
    
        

