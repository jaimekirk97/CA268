from student import who_searched

def test(lst):
    bst = BST()

    # Add each element in the lst to the tree
    for n in lst:
        bst.add(n)

    index = random.randint(0, len(lst) - 1)
    element = lst[index]

    elements = who_searched(element, bst)
    # Print the list and the result of calling the function
    print("search(" + str(element) + ", " + str(lst) +") is " + str(elements))

def main():
   random.seed(0)
   test([4])
   test([4, 5, 6, 7, 1, 2, 3])
   test([40, 20, 30, 50, 10, 13, 14, 5, 18])

if __name__ == '__main__':
    main()