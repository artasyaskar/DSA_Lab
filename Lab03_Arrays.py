class ArraySeq:
    def __init__(self):
        # Start with a small array of size 4, filled with zeros
        self.items = [0]*4
        # Number of valid elements (initially zero)
        self.size = 0
        # Track current array capacity
        self.capacity = 4

    def insert_last(self, item):
        # If array is full, resize (double the size)
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        # Add new item to the end
        self.items[self.size] = item
        # Increase valid element count
        self.size += 1

    def get_last(self):
        # If array is empty, return None
        if self.size == 0:
            return None
        # Else, return the last valid item
        return self.items[self.size - 1]

    def get_at(self, i):
        # Only allow valid indexes (0 ... size-1)
        if i < 0 or i >= self.size:
            return None
        return self.items[i]

    def length(self):
        # Number of valid elements
        return self.size

    def delete_last(self):
        # If array is empty, do nothing
        if self.size == 0:
            return
        # Remove last element (set to zero, optional for clarity)
        self.items[self.size - 1] = 0
        # Reduce count of valid elements
        self.size -= 1
        # If less than 25% full and capacity > 4, shrink array by half
        if self.size > 0 and self.size < self.capacity // 4 and self.capacity > 4:
            self.resize(self.capacity // 2)

    def resize(self, new_capacity):
        # Create a new array of the requested size
        new_items = [0]*new_capacity
        # Copy old values to the new array
        for i in range(self.size):
            new_items[i] = self.items[i]
        # Replace old items array and update capacity tracker
        self.items = new_items
        self.capacity = new_capacity

    def insert_at(self, index, item):
        # Checks if index is valid for insert (0 .. size)
        if index < 0 or index > self.size:
            return False
        # Resize, if array is full
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        # Shift elements to right from index onwards
        for i in range(self.size, index, -1):
            self.items[i] = self.items[i - 1]
        # Insert new item
        self.items[index] = item
        self.size += 1
        return True

    def delete_at(self, index):
        # Checks if index is valid for delete (0 .. size-1)
        if index < 0 or index >= self.size:
            return False
        # Shift elements left to fill the gap
        for i in range(index, self.size - 1):
            self.items[i] = self.items[i + 1]
        # Optional: Set now-unused last element to zero
        self.items[self.size - 1] = 0
        self.size -= 1
        # If less than 25% full and capacity > 4, shrink array
        if self.size > 0 and self.size < self.capacity // 4 and self.capacity > 4:
            self.resize(self.capacity // 2)
        return True

# --- Test code / Examples below ---
if __name__ == "__main__":
    # Create a new array sequence
    a = ArraySeq()
    print("Initial array:", a.items)
    a.insert_last(5)
    a.insert_last(10)
    a.insert_last(15)
    print("After insertions:", a.items)
    print("Last item:", a.get_last())
    print("Item at index 1:", a.get_at(1))
    print("Length:", a.length())
    a.delete_last()
    print("After delete_last:", a.items)
    a.insert_at(1, 20)
    print("After insert_at(1, 20):", a.items)
    a.delete_at(0)
    print("After delete_at(0):", a.items)
    # Resize checks
    for i in range(10):
        a.insert_last(i)
    print("After filling & resizing:", a.items)
    for i in range(11):
        a.delete_last()
    print("After multiple delete_last (shrinks):", a.items)
