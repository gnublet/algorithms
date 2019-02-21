class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree(root, spaces = 0, side = None):
    """
        Ghetto print function. 
        Right-to-left depth first traversal to print a tree flipped to the left
    """
    spacer_size = 3

    if root is None:
        return

    spaces += spacer_size

    # process right child
    print_tree(root.right, spaces, 'R')

    for i in range(spacer_size, spaces):
        print(" ", end="")

    if side == 'R': # Right node
        print("/ ", root.data)
    elif side == 'L': # Left node
        print("\ ", root.data) 
    else: # root node
        print(root.data)

    # process left child
    print_tree(root.left, spaces, 'L')

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.right = Node(12)
    print_tree(root)

main()