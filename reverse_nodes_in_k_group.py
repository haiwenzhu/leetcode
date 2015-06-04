# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://leetcode.com/problems/reverse-nodes-in-k-group/
    """
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        node = head 
        head = None
        knode = None
        pre_node = None
        i = 1
        while node:
            if i%k == 0:
                if not head:
                    head = node
                else:
                    pre_knode.next = node
            elif i%k == 1:
                pre_knode = knode
                knode = node
                pre_node = None
            next = node.next
            node.next = pre_node
            pre_node = node
            node = next
            i += 1
        i -= 1
        if i%k != 0:
            node = pre_node
            pre_node = None
            while node:
                next = node.next
                node.next = pre_node
                pre_node = node
                node = next
            if i > k:
                pre_knode.next = knode
            else:
                head = knode
        return head

if __name__ == "__main__":
    solution = Solution()
    from lib import list
    l = list.List([1,2,3,4,5,6])
    l = list.List([1,2])
    print(solution.reverseKGroup(l.head, 1))
