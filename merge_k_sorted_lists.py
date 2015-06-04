# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @see https://leetcode.com/problems/merge-k-sorted-lists/
    """
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        #filter empty list
        lists1 = []
        for item in lists:
            if item:
                lists1.append(item)
        lists = lists1
        length = len(lists)
        if length == 0:
            return None
        lists = sorted(lists, key=lambda node: node.val)
        head = lists[0]
        node = lists[0]
        while length > 1:
            next_val = lists[1].val
            while node.next and node.next.val <= next_val:
                node = node.next
            lists.pop(0)
            if node.next:
                inserted = False
                for i, v in enumerate(lists):
                    if node.next.val <= v.val:
                        lists.insert(i, node.next)
                        inserted = True
                        break
                if not inserted:
                    lists.append(node.next)
            else:
                length -= 1
            node.next = lists[0]
            node = node.next
        return head 

if __name__ == "__main__":
    from lib import list
    solution = Solution()
    l1 = list.List([1,7,10,15])
    l2 = list.List([1,2,5,8])
    l3 = list.List([0,10,20])
    print(solution.mergeKLists([l1.head, l2.head, l3.head]))
    print(solution.mergeKLists([None,None]))
