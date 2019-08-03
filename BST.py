class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)

    def rheight(self,ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.rheight(ptr.left), self.rheight(ptr.right))

    def height(self):
        return self.rheight(self.root)

    def rcount_leaves(self, ptr):
        if ptr == None:
            return 0
        elif ptr.left == None and ptr.right == None:
            return 1 + self.rcount_leaves(ptr.left) + self.rcount_leaves(ptr.right)
        return self.rcount_leaves(ptr.left) + self.rcount_leaves(ptr.right)

    def count_leaves(self):
        return self.rcount_leaves(self.root)