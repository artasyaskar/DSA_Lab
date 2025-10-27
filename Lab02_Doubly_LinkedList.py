# Node class for doubly linked list
class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item        # Store data value
        self.prev = prev        # Pointer to previous node
        self.next = next        # Pointer to next node

# Doubly linked list with sentinel node
class DLList:
    def __init__(self):
        # Create sentinel node (doesn't store data, helps handle edge cases)
        self.sentinel = Node(None)
        # Sentinel's next and prev point to itself (empty list)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.len = 0           # Track number of elements in list

    # Check if list is empty
    def is_empty(self):
        return self.len == 0

    # Insert at front (right after sentinel)
    def insert_first(self, item):
        new_node = Node(item)
        # Links for new_node
        new_node.next = self.sentinel.next
        new_node.prev = self.sentinel
        # Adjust existing front node's prev pointer
        self.sentinel.next.prev = new_node
        # Sentinel's next pointer is updated
        self.sentinel.next = new_node
        self.len += 1

    # Insert at end (right before sentinel)
    def insert_last(self, item):
        new_node = Node(item)
        new_node.next = self.sentinel
        new_node.prev = self.sentinel.prev
        self.sentinel.prev.next = new_node
        self.sentinel.prev = new_node
        self.len += 1

    # Remove and return first element
    def delete_first(self):
        if self.is_empty():
            raise IndexError("List is empty!")
        first_node = self.sentinel.next
        item = first_node.item
        self.sentinel.next = first_node.next
        first_node.next.prev = self.sentinel
        self.len -= 1
        return item

    # Remove and return last element
    def delete_last(self):
        if self.is_empty():
            raise IndexError("List is empty!")
        last_node = self.sentinel.prev
        item = last_node.item
        self.sentinel.prev = last_node.prev
        last_node.prev.next = self.sentinel
        self.len -= 1
        return item

    # Get the item at a given index (0-based)
    def get_at(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        current = self.sentinel.next
        for _ in range(index):
            current = current.next
        return current.item

    # Return length of list
    def __len__(self):
        return self.len

    # Convert whole list to a Python list for easy viewing
    def to_list(self):
        result = []
        current = self.sentinel.next
        while current != self.sentinel:
            result.append(current.item)
            current = current.next
        return result

    # For debugging, print all elements nicely
    def __str__(self):
        return ' <-> '.join(str(item) for item in self.to_list())

# ========== TEST CODE (safe to run as a beginner, shows outputs) ==========
if __name__ == "__main__":
    dll = DLList()
    print("Is empty?", dll.is_empty())   # Yes, should be True

    print("\nAdding 10, 20 at front:")
    dll.insert_first(10)
    dll.insert_first(20)
    print("List now:", dll)              # Should show: 20 <-> 10

    print("\nAdding 30 at end:")
    dll.insert_last(30)
    print("List now:", dll)              # Should show: 20 <-> 10 <-> 30

    print("\nDelete first (should remove 20):")
    print("Deleted:", dll.delete_first()) # Removes 20
    print("List now:", dll)               # 10 <-> 30

    print("\nDelete last (should remove 30):")
    print("Deleted:", dll.delete_last())
    print("List now:", dll)               # 10

    print("\nAccess first (index 0):", dll.get_at(0)) # 10
    print("Current length (should be 1):", len(dll))

    print("\nConvert to Python list:", dll.to_list())
