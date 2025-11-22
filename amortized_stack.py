# ---------------------------------------------------------
# Stack with Dynamic Array (Amortized Analysis)
# - Doubles size when full
# - Halves size when 1/4 full
# ---------------------------------------------------------

class DynamicStack:
    def __init__(self):
        self.stack = [None] * 2   # initial capacity
        self.size = 0

    def resize(self, new_cap):
        new_arr = [None] * new_cap
        for i in range(self.size):
            new_arr[i] = self.stack[i]
        self.stack = new_arr
        print(f"[Resize] New capacity = {new_cap}")

    def push(self, value):
        if self.size == len(self.stack):
            self.resize(len(self.stack) * 2)

        self.stack[self.size] = value
        self.size += 1
        print(f"Pushed: {value} | Size: {self.size}")

    def pop(self):
        if self.size == 0:
            print("Stack is empty!")
            return None

        value = self.stack[self.size - 1]
        self.size -= 1
        print(f"Popped: {value} | Size: {self.size}")

        # shrink if size is 1/4 of capacity
        if self.size > 0 and self.size == len(self.stack) // 4:
            self.resize(len(self.stack) // 2)

        return value


# ---------------------------------------------------------
# MAIN (User Input Only)
# ---------------------------------------------------------
if __name__ == "__main__":

    stack = DynamicStack()

    print("\n=== Dynamic Stack (Amortized Analysis) ===")
    print("Commands:")
    print(" push X  -> push value")
    print(" pop     -> pop top")
    print(" exit    -> stop program\n")

    while True:
        command = input("Enter command: ").strip().lower()

        if command.startswith("push"):
            try:
                _, val = command.split()
                stack.push(int(val))
            except:
                print("Invalid push command! Use: push <value>")

        elif command == "pop":
            stack.pop()

        elif command == "exit":
            print("Exiting...")
            break

        else:
            print("Invalid command!")
