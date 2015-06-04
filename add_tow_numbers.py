# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/add-two-numbers/
    """
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        pre = None
        inc = 0
        head = None
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + inc
            inc = val // 10
            val = val % 10
            node = ListNode(val)
            if pre:
                pre.next = node
            if not head:
                head = node
            pre = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if inc > 0:
            pre.next = ListNode(inc)

        return head 

if __name__ == "__main__":
    from lib import list
    solution = Solution()
    print(list.List.parseNode(solution.addTwoNumbers(list.List([1, 8]).head, list.List([0]).head)))
        

