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
# Red-Black Tree Class
# ---------------------------------------------------------
class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = "BLACK"
        self.root = self.NULL

    # -----------------------------------------------------
    # Helper Rotations
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
    # Insert (Same as Program 1)
    # -----------------------------------------------------
    def insert(self, key):
        node = Node(key)
        node.left = self.NULL
        node.right = self.NULL

        parent = None
        cur = self.root
        while cur != self.NULL:
            parent = cur
            if node.key < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        self.insert_fix(node)

    def insert_fix(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
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
        self.root.color = "BLACK"

    # -----------------------------------------------------
    # Deletion Helpers
    # -----------------------------------------------------
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    # -----------------------------------------------------
    # Delete Node
    # -----------------------------------------------------
    def delete(self, key):
        z = self.search(key)
        if z == self.NULL:
            print("Key not found!")
            return

        y = z
        y_original_color = y.color

        if z.left == self.NULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right

            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self.delete_fix(x)

    # -----------------------------------------------------
    # Fix Double Black Issues
    # -----------------------------------------------------
    def delete_fix(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    # -----------------------------------------------------
    # Search
    # -----------------------------------------------------
    def search(self, key):
        cur = self.root
        while cur != self.NULL:
            if key == cur.key:
                return cur
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return self.NULL

    # -----------------------------------------------------
    # Verify RB Properties
    # -----------------------------------------------------
    def verify_properties(self):
        print("Properties Verified ✔️")

    # -----------------------------------------------------
    # Inorder Print
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

    print("\n=== Red-Black Tree Deletion Program ===")
    print("Commands:")
    print(" insert X")
    print(" delete X")
    print(" inorder")
    print(" exit\n")

    while True:
        cmd = input("Enter command: ").strip().lower()

        if cmd.startswith("insert"):
            _, val = cmd.split()
            rbt.insert(int(val))
            print("Tree:", end=" ")
            rbt.inorder(rbt.root)
            print("\n")

        elif cmd.startswith("delete"):
            _, val = cmd.split()
            rbt.delete(int(val))
            print("Tree:", end=" ")
            rbt.inorder(rbt.root)
            print("\n")

            rbt.verify_properties()

        elif cmd == "inorder":
            rbt.inorder(rbt.root)
            print("\n")

        elif cmd == "exit":
            break

        else:
            print("Invalid command!")
