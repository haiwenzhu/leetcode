# Definition for a  binary tree node
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        nodes = [self]
        s = '' 
        while nodes:
            node = nodes.pop(0)
            if node:
                s += ', ' + str(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                s += ', #'
        return s[2:]
    def toList(self):
        nodes = [self]
        l = [] 
        while nodes:
            node = nodes.pop(0)
            if node:
                l.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                l.append('#')
        return l

class TreeParser:
    def parse(self, vals):
        i = 0
        length = len(vals)
        if length == 0:
            return None

        root = TreeNode(vals[i])
        nodes = collections.deque([root])
        while nodes:
            node = nodes.popleft()
            i += 1
            if i < length:
                if vals[i] != '#':
                    node.left = TreeNode(vals[i])
                    nodes.append(node.left)
                i += 1
                if i < length:
                    if vals[i] != '#':
                        node.right = TreeNode(vals[i])
                        nodes.append(node.right)
                else:
                    break
            else:
                break
        
        return root
