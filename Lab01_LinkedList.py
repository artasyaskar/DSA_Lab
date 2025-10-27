# Node class represents a single node of the linked list
class Node:
    def __init__(self, item, next=None):
        self.item = item      # The actual data stored in this node
        self.next = next      # Points to the next node in the list (None by default)

# SLList stands for Singly Linked List
class SLList:
    def __init__(self):
        # Sentinel node: a dummy node at the start that helps with edge cases
        self.sentinel = Node(None) 
        # Number of real nodes (not counting the sentinel)
        self.length = 0  

    def insert_first(self, item):
        # Create a new node whose next node is the current first data node
        new_node = Node(item, self.sentinel.next)
        # The sentinel's next is updated to point to this new node (now at the front)
        self.sentinel.next = new_node
        # Increase the length to count the new node
        self.length += 1

    def insert_last(self, item):
        # Start at the sentinel node (does not hold data)
        current = self.sentinel
        # Move forward until we reach the last real node (whose .next is None)
        while current.next:
            current = current.next
        # Attach a new node at the end
        current.next = Node(item)
        self.length += 1  # Increase length for this new node

    def insert_at(self, i, item):
        # i is the index where you want to insert the new data node
        if i < 0 or i > self.length:
            # If index is out-of-bounds, raise an error
            raise IndexError("Index out of bounds")
        # Start at the sentinel
        current = self.sentinel
        # Move to the node just before position i
        for _ in range(i):
            current = current.next
        # Create a node and link it into position
        new_node = Node(item, current.next)
        current.next = new_node
        self.length += 1  # Update count

    def get_first(self):
        # If there are no actual nodes, return None
        if not self.sentinel.next:
            return None
        # Return the item of the first real node (right after sentinel)
        return self.sentinel.next.item

    def len(self):
        # Return the number of data nodes
        return self.length

    def display(self):
        # Start at the first real node (after sentinel)
        items = []  # List to collect node values
        current = self.sentinel.next
        # Traverse through all nodes
        while current:
            items.append(str(current.item))  # Add the data to list
            current = current.next           # Move to next node
        print("Linked List:", " -> ".join(items))

# --------------- Test Code ---------------

# Create an empty list
lst = SLList()

# Insert an item at the front (should be first in the list)
lst.insert_first(10)
lst.display()         # Output: 10

# Insert another at the front (becomes new first)
lst.insert_first(20)
lst.display()         # Output: 20 -> 10

# Insert an item at the end (should be last)
lst.insert_last(30)
lst.display()         # Output: 20 -> 10 -> 30

# Insert at position 1 (after first node: index 0, so after '20')
lst.insert_at(1, 99)
lst.display()         # Output: 20 -> 99 -> 10 -> 30

# Get the first element
print("First element:", lst.get_first())      # Output: 20

# Get the length of the list
print("List length:", lst.len())              # Output: 4

# If you want to test more, try removing, searching, etc., or asking for new methods!
