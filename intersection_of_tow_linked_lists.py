# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://oj.leetcode.com/problems/intersection-of-two-linked-lists/
    """
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = 0
        lenB = 0

        node = headA
        while node:
            lenA += 1
            node = node.next

        node = headB
        while node:
            lenB += 1
            node = node.next
        
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next

        while headA and headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA

if __name__ == "__main__":
    from lib import list
    solution = Solution()

    listA = list.List([1,2])
    listB = list.List([1])
    listC = list.List([3,4])

    tailA = listA.head
    while tailA.next:
        tailA = tailA.next
    tailA.next = listC.head

    tailB = listB.head
    while tailB.next:
        tailB = tailB.next
    tailB.next = listC.head

    print(solution.getIntersectionNode(listA.head, None))

