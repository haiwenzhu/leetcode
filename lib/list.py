# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        node = self
        while node:
            if s == '':
                s = str(node.val)
            else:
                s += '->' + str(node.val)
            node = node.next
        return s


class List:
    def __init__(self, vals):
        if len(vals) == 0:
            self.head = None
        else:
            self.head = ListNode(vals[0])
            pre = self.head 
            for i in range(1, len(vals)):
                pre.next = ListNode(vals[i])
                pre = pre.next

    def __str__(self):
        s = ''
        node = self.head
        while node:
            if s == '':
                s = str(node.val)
            else:
                s = '->' + str(node.val)
            node = node.next
        return s

    @staticmethod
    def parseNode(node):
        s = ''
        while node:
            if s == '':
                s = str(node.val)
            else:
                s += '->' + str(node.val)
            node = node.next
        return s


