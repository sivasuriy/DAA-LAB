# ---------------------------------------------------------
# Binomial Node
# ---------------------------------------------------------
class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.sibling = None
        self.degree = 0


# ---------------------------------------------------------
# Binomial Heap
# ---------------------------------------------------------
class BinomialHeap:
    def __init__(self):
        self.head = None

    # -----------------------------------------------------
    # Merge two binomial trees of same degree
    # -----------------------------------------------------
    def merge_tree(self, t1, t2):
        if t1.key > t2.key:
            t1, t2 = t2, t1

        t2.parent = t1
        t2.sibling = t1.child
        t1.child = t2
        t1.degree += 1
        return t1

    # -----------------------------------------------------
    # Merge two root lists
    # -----------------------------------------------------
    def merge_root_lists(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        head = None
        tail = None

        while h1 and h2:
            if h1.degree <= h2.degree:
                min_node = h1
                h1 = h1.sibling
            else:
                min_node = h2
                h2 = h2.sibling

            if head is None:
                head = min_node
                tail = min_node
            else:
                tail.sibling = min_node
                tail = min_node

        while h1:
            tail.sibling = h1
            tail = h1
            h1 = h1.sibling

        while h2:
            tail.sibling = h2
            tail = h2
            h2 = h2.sibling

        return head

    # -----------------------------------------------------
    # Union two heaps into one valid heap
    # -----------------------------------------------------
    def union(self, h2):
        new_head = self.merge_root_lists(self.head, h2.head)
        if new_head is None:
            return

        prev = None
        curr = new_head
        next = curr.sibling

        while next is not None:
            if curr.degree != next.degree or \
               (next.sibling is not None and next.sibling.degree == curr.degree):
                prev = curr
                curr = next
            else:
                if curr.key <= next.key:
                    curr.sibling = next.sibling
                    self.merge_tree(curr, next)
                else:
                    if prev is None:
                        new_head = next
                    else:
                        prev.sibling = next
                    self.merge_tree(next, curr)
                    curr = next
            next = curr.sibling

        self.head = new_head

    # -----------------------------------------------------
    # Insert operation
    # -----------------------------------------------------
    def insert(self, key):
        new_heap = BinomialHeap()
        new_node = BinomialNode(key)
        new_heap.head = new_node
        self.union(new_heap)

    # -----------------------------------------------------
    # Display heap (level order)
    # -----------------------------------------------------
    def print_heap(self):
        print("\nBinomial Heap:")

        def print_tree(node, depth):
            while node:
                print("  " * depth + f"- {node.key} (deg {node.degree})")
                if node.child:
                    print_tree(node.child, depth + 1)
                node = node.sibling

        if self.head is None:
            print("[empty]")
        else:
            print_tree(self.head, 0)
        print("")


# ---------------------------------------------------------
# MAIN (User Input)
# ---------------------------------------------------------
if __name__ == "__main__":
    heap = BinomialHeap()

    print("\n=== Binomial Heap (Insert + Merge) ===")
    print("Commands:")
    print(" insert X")
    print(" show")
    print(" exit\n")

    while True:
        cmd = input("Enter command: ").strip().lower()

        if cmd.startswith("insert"):
            try:
                _, val = cmd.split()
                heap.insert(int(val))
                print("Inserted:", val)
                heap.print_heap()
            except:
                print("Invalid input! Use: insert <value>")

        elif cmd == "show":
            heap.print_heap()

        elif cmd == "exit":
            break

        else:
            print("Invalid command!")
