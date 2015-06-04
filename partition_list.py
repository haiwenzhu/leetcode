# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        lastNode = None
        preNode = None
        node = head
        while node:
            if node.val < x:
                if lastNode == preNode:
                    lastNode = node
                    preNode = node
                else:
                    preNode.next = node.next
                    if lastNode:
                        node.next = lastNode.next
                        lastNode.next = node
                        lastNode = node
                    else:
                        node.next = head
                        lastNode = node
                        head = lastNode
            else:
                preNode = node
            node = preNode.next
        return head

if __name__ == "__main__":
    solution = Solution()
    from lib import list
    l = list.List([1,4,3,2,5,2])
    print(solution.partition(l.head, 3))
