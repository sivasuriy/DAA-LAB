# ---------------------------------------------------------
# Dynamic Table Simulation (Array Doubling + Shrinking)
# Amortized Analysis:
# - Double size when full
# - Shrink to half when less than half full
# - Track number of element movements
# ---------------------------------------------------------

class DynamicTable:
    def __init__(self):
        self.table = [None] * 2   # initial capacity
        self.size = 0
        self.movements = 0        # count element moves

    def resize(self, new_cap):
        new_arr = [None] * new_cap
        for i in range(self.size):
            new_arr[i] = self.table[i]
            self.movements += 1   # each copy counts as movement
        self.table = new_arr
        print(f"[Resize] New capacity = {new_cap}, Total movements = {self.movements}")

    def insert(self, value):
        if self.size == len(self.table):
            self.resize(len(self.table) * 2)

        self.table[self.size] = value
        self.size += 1
        print(f"Inserted: {value} | Size = {self.size}")

    def delete(self):
        if self.size == 0:
            print("Table is empty!")
            return None

        removed = self.table[self.size - 1]
        self.size -= 1
        print(f"Deleted: {removed} | Size = {self.size}")

        # shrink when size < half capacity
        if self.size > 0 and self.size <= len(self.table) // 2:
            self.resize(len(self.table) // 2)

        return removed


# ---------------------------------------------------------
# MAIN (User Input Only)
# ---------------------------------------------------------
if __name__ == "__main__":

    table = DynamicTable()

    print("\n=== Dynamic Table Simulation (Amortized Analysis) ===")
    print("Commands:")
    print(" insert X  -> insert value")
    print(" delete    -> delete last value")
    print(" exit      -> stop program\n")

    while True:
        command = input("Enter command: ").strip().lower()

        if command.startswith("insert"):
            try:
                _, val = command.split()
                table.insert(int(val))
            except:
                print("Invalid command! Use: insert <value>")

        elif command == "delete":
            table.delete()

        elif command == "exit":
            print("Exiting...")
            break

        else:
            print("Invalid command!")
