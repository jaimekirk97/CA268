#
#   Determine which elements are visited while searching for a particular value
#
def rwho_searched(val, bst):
    ptr = bst.root
    if ptr == None:
        return False
    elif num == ptr.item:
        return True
    elif num < ptr.item:
        return self.r_present(ptr.left, num)
    else:
        return self.r_present(ptr.right, num)
    return False

def who_searched(val, bst):
    return bst.rwho_searched(val)
    