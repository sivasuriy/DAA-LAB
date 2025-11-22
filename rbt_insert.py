# ---------------------------------------------------------
# Red-Black Tree Node
# ---------------------------------------------------------
class Node:
    def __init__(self, key):
        self.key = key
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

# ---------------------------------------------------------
# Red-Black Tree
# ---------------------------------------------------------
class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = "BLACK"
        self.root = self.NULL

    # -----------------------------------------------------
    # Left Rotate
    # -----------------------------------------------------
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # -----------------------------------------------------
    # Right Rotate
    # -----------------------------------------------------
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # -----------------------------------------------------
    # Insert Fix (fix violations)
    # -----------------------------------------------------
    def fix_insert(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # uncle
                if y.color == "RED":
                    # Case 1: recolor
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    # Case 2/3: rotations
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)

            else:  # mirror case
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)

            if z == self.root:
                break

        self.root.color = "BLACK"

    # -----------------------------------------------------
    # Insert
    # -----------------------------------------------------
    def insert(self, key):
        node = Node(key)
        node.left = self.NULL
        node.right = self.NULL

        parent = None
        current = self.root

        # Normal BST insertion
        while current != self.NULL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        # fix violation
        self.fix_insert(node)

    # -----------------------------------------------------
    # Inorder Traversal (to show balanced tree)
    # -----------------------------------------------------
    def inorder(self, node):
        if node != self.NULL:
            self.inorder(node.left)
            print(f"{node.key} ({node.color})", end="  ")
            self.inorder(node.right)


# ---------------------------------------------------------
# MAIN (User Input)
# ---------------------------------------------------------
if __name__ == "__main__":
    rbt = RedBlackTree()

    print("\n=== Red-Black Tree Insertion ===")
    print("Enter numbers to insert (type 'done' to stop):")

    while True:
        val = input("Insert: ").strip()
        if val.lower() == "done":
            break
        try:
            rbt.insert(int(val))
            print("Current Tree (Inorder): ", end="")
            rbt.inorder(rbt.root)
            print("\n")
        except:
            print("Invalid input!")
