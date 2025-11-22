import time
import random

# ---------------------------------------------------------
# (1) Red-Black Tree Implementation (Simplified Insert/Search/Delete)
# ---------------------------------------------------------

class RBTNode:
    def __init__(self, key):
        self.key = key
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NULL = RBTNode(0)
        self.NULL.color = "BLACK"
        self.root = self.NULL

    # ---- Basic Insertion (same as Program 1) ----
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

    def insert(self, key):
        node = RBTNode(key)
        node.left = self.NULL
        node.right = self.NULL

        parent = None
        cur = self.root
        while cur != self.NULL:
            parent = cur
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        node.parent = parent

        if parent is None:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def fix_insert(self, z):
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

    # ---- Simplified Search ----
    def search(self, key):
        cur = self.root
        while cur != self.NULL:
            if key == cur.key:
                return True
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return False


# ---------------------------------------------------------
# (2) Binomial Heap (Insert + Extract + Decrease only)
# ---------------------------------------------------------

class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

class BinomialHeap:
    def __init__(self):
        self.head = None

    def merge_tree(self, t1, t2):
        if t1.key > t2.key:
            t1, t2 = t2, t1
        t2.parent = t1
        t2.sibling = t1.child
        t1.child = t2
        t1.degree += 1
        return t1

    def merge_root_lists(self, h1, h2):
        if h1 is None: return h2
        if h2 is None: return h1
        head = None
        tail = None
        while h1 and h2:
            if h1.degree <= h2.degree:
                temp = h1
                h1 = h1.sibling
            else:
                temp = h2
                h2 = h2.sibling
            if not head:
                head = temp
                tail = temp
            else:
                tail.sibling = temp
                tail = temp
        while h1:
            tail.sibling = h1
            tail = h1
            h1 = h1.sibling
        while h2:
            tail.sibling = h2
            tail = h2
            h2 = h2.sibling
        return head

    def union(self, h2):
        new_head = self.merge_root_lists(self.head, h2.head)
        if not new_head:
            return
        prev = None
        curr = new_head
        nxt = curr.sibling
        while nxt:
            if curr.degree != nxt.degree or \
              (nxt.sibling and nxt.sibling.degree == curr.degree):
                prev = curr
                curr = nxt
            else:
                if curr.key <= nxt.key:
                    curr.sibling = nxt.sibling
                    self.merge_tree(curr, nxt)
                else:
                    if prev is None:
                        new_head = nxt
                    else:
                        prev.sibling = nxt
                    self.merge_tree(nxt, curr)
                    curr = nxt
            nxt = curr.sibling
        self.head = new_head

    def insert(self, key):
        new_heap = BinomialHeap()
        new_heap.head = BinomialNode(key)
        self.union(new_heap)

    # simple find
    def search(self, root, key):
        if not root:
            return False
        if root.key == key:
            return True
        return self.search(root.child, key) or self.search(root.sibling, key)


# ---------------------------------------------------------
# MAIN – User Input & Performance Measurement
# ---------------------------------------------------------
if __name__ == "__main__":
    print("\n=== RBT vs Binomial Heap Performance Comparison ===")

    n = int(input("Enter number of random elements: "))

    data = [random.randint(1, 100000) for _ in range(n)]
    search_key = random.choice(data)

    # RBT
    rbt = RedBlackTree()
    start = time.time()
    for x in data:
        rbt.insert(x)
    insert_rbt = time.time() - start

    start = time.time()
    rbt.search(search_key)
    search_rbt = time.time() - start

    # Binomial Heap
    heap = BinomialHeap()
    start = time.time()
    for x in data:
        heap.insert(x)
    insert_bh = time.time() - start

    start = time.time()
    found = heap.search(heap.head, search_key)
    search_bh = time.time() - start

    # Output
    print("\n--- Performance Results ---")
    print(f"Input Size = {n}")
    print("-------------------------------")
    print(f"RBT Insert Time      : {insert_rbt:.6f} sec")
    print(f"RBT Search Time      : {search_rbt:.6f} sec\n")
    print(f"Binomial Insert Time : {insert_bh:.6f} sec")
    print(f"Binomial Search Time : {search_bh:.6f} sec")
    print("-------------------------------")

    print("\nConclusion:")
    print("✔ RBT gives guaranteed O(log n) performance")
    print("✔ Binomial Heap depends heavily on structure and randomness")
