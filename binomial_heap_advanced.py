# ---------------------------------------------------------
# Binomial Node
# ---------------------------------------------------------
class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None


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
    # Merge root lists
    # -----------------------------------------------------
    def merge_root_lists(self, h1, h2):
        if not h1: return h2
        if not h2: return h1

        head = None
        tail = None

        while h1 and h2:
            if h1.degree <= h2.degree:
                min_node = h1
                h1 = h1.sibling
            else:
                min_node = h2
                h2 = h2.sibling

            if not head:
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
    # Union two heaps
    # -----------------------------------------------------
    def union(self, heap2):
        new_head = self.merge_root_lists(self.head, heap2.head)

        if new_head is None:
            return

        prev = None
        curr = new_head
        next = curr.sibling

        while next:
            if (curr.degree != next.degree) or \
               (next.sibling and next.sibling.degree == curr.degree):
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
    # Insert key
    # -----------------------------------------------------
    def insert(self, key):
        new_heap = BinomialHeap()
        new_heap.head = BinomialNode(key)
        self.union(new_heap)

    # -----------------------------------------------------
    # Find minimum root
    # -----------------------------------------------------
    def get_min_node(self):
        if self.head is None:
            return None, None

        min_node = self.head
        min_prev = None
        prev = self.head
        curr = self.head.sibling

        while curr:
            if curr.key < min_node.key:
                min_node = curr
                min_prev = prev
            prev = curr
            curr = curr.sibling

        return min_prev, min_node

    # -----------------------------------------------------
    # Extract-Min
    # -----------------------------------------------------
    def extract_min(self):
        if not self.head:
            print("Heap is empty!")
            return None

        min_prev, min_node = self.get_min_node()

        # Remove min_node from root list
        if min_prev:
            min_prev.sibling = min_node.sibling
        else:
            self.head = min_node.sibling

        # Reverse its children into a new heap
        child = min_node.child
        new_head = None
        while child:
            next = child.sibling
            child.sibling = new_head
            child.parent = None
            new_head = child
            child = next

        new_heap = BinomialHeap()
        new_heap.head = new_head

        self.union(new_heap)

        return min_node.key

    # -----------------------------------------------------
    # Decrease-Key
    # -----------------------------------------------------
    def decrease_key(self, old_key, new_key):
        if new_key > old_key:
            print("New key must be smaller.")
            return

        node = self.find(self.head, old_key)
        if not node:
            print("Key not found!")
            return

        node.key = new_key
        parent = node.parent

        while parent and node.key < parent.key:
            node.key, parent.key = parent.key, node.key
            node = parent
            parent = node.parent

    # -----------------------------------------------------
    # Find a key (DFS)
    # -----------------------------------------------------
    def find(self, root, key):
        if not root:
            return None
        if root.key == key:
            return root

        res = self.find(root.child, key)
        if res:
            return res

        return self.find(root.sibling, key)

    # -----------------------------------------------------
    # Print heap structure
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
# MAIN (User Input Only)
# ---------------------------------------------------------
if __name__ == "__main__":
    heap = BinomialHeap()

    print("\n=== Binomial Heap Advanced (Extract-Min + Decrease-Key) ===")
    print("Commands:")
    print(" insert X")
    print(" extract")
    print(" decrease old new")
    print(" show")
    print(" exit\n")

    while True:
        cmd = input("Enter command: ").strip().lower()

        if cmd.startswith("insert"):
            _, x = cmd.split()
            heap.insert(int(x))
            print(f"Inserted {x}")
            heap.print_heap()

        elif cmd == "extract":
            val = heap.extract_min()
            if val is not None:
                print("Extracted Min:", val)
            heap.print_heap()

        elif cmd.startswith("decrease"):
            try:
                _, old, new = cmd.split()
                heap.decrease_key(int(old), int(new))
                print(f"Decreased {old} → {new}")
                heap.print_heap()
            except:
                print("Invalid command! Use: decrease <old> <new>")

        elif cmd == "show":
            heap.print_heap()

        elif cmd == "exit":
            break

        else:
            print("Invalid command!")
