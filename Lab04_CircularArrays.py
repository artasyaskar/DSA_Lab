class Aseq:
    def __init__(self):
        # Initialize array with default capacity of 4 (can change this value)
        self._array = [None] * 4
        # Number of actual elements currently in sequence
        self._size = 0
        # Maximum capacity before needing to resize
        self._capacity = 4
        # Index of the front of the sequence
        self._front = 0
        # Index of the back of the sequence (-1 initially means empty)
        self._back = -1

    def insert_first(self, value):
        # Check if array needs to be resized (doubled) before adding
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        # Move front pointer circularly backward
        self._front = (self._front - 1) % self._capacity
        # Insert the new value at the front
        self._array[self._front] = value
        # If inserting into empty sequence, update back pointer too
        if self._size == 0:
            self._back = self._front
        # Increase the count of elements
        self._size += 1

    def insert_last(self, value):
        # Check if array needs resizing before adding
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        # Move back pointer circularly forward
        self._back = (self._back + 1) % self._capacity
        # Insert the new value at the back
        self._array[self._back] = value
        # If sequence was empty, front pointer should match back
        if self._size == 0:
            self._front = self._back
        # Increase the count of elements
        self._size += 1

    def _resize(self, new_capacity):
        # Create a new array with the new capacity
        new_array = [None] * new_capacity
        # Copy elements from the old array to new array in correct order
        for i in range(self._size):
            # Compute the real index using circular logic
            new_array[i] = self._array[(self._front + i) % self._capacity]
        # Update pointers
        self._array = new_array
        self._capacity = new_capacity
        self._front = 0
        # Back is now at the last element
        self._back = self._size - 1 if self._size > 0 else -1

    def get_at(self, i):
        # Return None if index is out of bounds
        if i < 0 or i >= self._size:
            return None
        # Compute circular array index
        index = (self._front + i) % self._capacity
        # Return the item at that index
        return self._array[index]

    def is_empty(self):
        # True if sequence has no elements
        return self._size == 0

    def length(self):
        # Number of actual elements in sequence
        return self._size

    def toList(self):
        # Create a regular Python list
        result = []
        # Add each element in the correct logical order
        for i in range(self._size):
            result.append(self._array[(self._front + i) % self._capacity])
        return result

    def insert_at(self, index, value):
        # Insert 'value' at position 'index': shift elements right
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds!")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        # If inserting at front/back, use existing methods
        if index == 0:
            self.insert_first(value)
            return
        if index == self._size:
            self.insert_last(value)
            return
        # Find position to insert, shift elements right
        insert_pos = (self._front + index) % self._capacity
        curr = self._back
        # Move all elements one step forward (from back to insert_pos)
        while curr != insert_pos:
            next_pos = (curr + 1) % self._capacity
            self._array[next_pos] = self._array[curr]
            curr = (curr - 1) % self._capacity
        self._array[insert_pos] = value
        self._back = (self._back + 1) % self._capacity
        self._size += 1

    def delete_at(self, index):
        # Delete the element at position 'index'
        if self.is_empty() or index < 0 or index >= self._size:
            raise IndexError("Index out of bounds or sequence empty!")
        # If removing from front or back, shortcut
        if index == 0:
            # Remove from front
            self._array[self._front] = None
            self._front = (self._front + 1) % self._capacity
            self._size -= 1
            if self._size == 0:
                self._back = -1
            return
        elif index == self._size - 1:
            # Remove from back
            self._array[self._back] = None
            self._back = (self._back - 1) % self._capacity
            self._size -= 1
            if self._size == 0:
                self._front = 0
            return
        # If removing from middle, shift elements left
        remove_pos = (self._front + index) % self._capacity
        curr = remove_pos
        while curr != self._back:
            next_pos = (curr + 1) % self._capacity
            self._array[curr] = self._array[next_pos]
            curr = next_pos
        self._array[self._back] = None
        self._back = (self._back - 1) % self._capacity
        self._size -= 1
        # Resize down if usage is less than 25%
        if 0 < self._size < self._capacity // 4 and self._capacity > 4:
            self._resize(max(4, self._capacity // 2))


# Example usage and test code to help you understand:
if __name__ == "__main__":
    seq = Aseq()
    seq.insert_last(5)
    seq.insert_last(10)
    seq.insert_first(15)
    print(seq.toList())  # prints [15, 5, 10]

    seq.insert_at(1, 8)  # Inserts 8 at position 1: [15, 8, 5, 10]
    print(seq.toList())

    seq.delete_at(2)     # Removes item at position 2: [15, 8, 10]
    print(seq.toList())

    print("First item:", seq.get_at(0))
    print("Is empty?", seq.is_empty())
    print("Length:", seq.length())
