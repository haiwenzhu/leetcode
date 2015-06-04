# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/reverse-linked-list-ii/
    """
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        beforeStart = None
        start = None
        preNode = None
        pos = 1
        node = head
        while node:
            nextNode = node.next
            if pos == m-1:
                beforeStart = node
            elif pos == m:
                start = node
            elif pos > m and pos <= n:
                node.next = preNode
                if pos == n:
                    if beforeStart:
                        beforeStart.next = node
                    else:
                        head = node
                    start.next = nextNode
                    break
            preNode = node
            node = nextNode
            pos += 1
        return head

if __name__ == "__main__":
    solution = Solution()
    from lib import list
    l = list.List([1,2,3,4,5])
    print(solution.reverseBetween(l.head, 2, 2))
