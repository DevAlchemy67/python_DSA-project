"""
Data Structures Implementation for DSA Practice
"""

class Node:
    """Base node class for linked structures."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Linked List: O(1) insertion/deletion at head, O(n) at tail
    A linear data structure where each element points to the next.
    """
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        """Add element at the end."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add element at the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Delete first occurrence of data."""
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def search(self, data):
        """Search for data, return True if found."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        """Display the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty"
    
    def __str__(self):
        return self.display()


class Stack:
    """
    Stack: LIFO (Last In First Out)
    O(1) for push, pop, and peek operations.
    """
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        """Add element to the top of the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    
    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


class Queue:
    """
    Queue: FIFO (First In First Out)
    O(1) for enqueue and dequeue operations.
    """
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add element to the end of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
    
    def front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]
    
    def size(self):
        """Return the number of elements in the queue."""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


class TreeNode:
    """Node for binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree: O(log n) average, O(n) worst case for operations
    A binary tree where left child < parent < right child.
    """
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert data into the BST."""
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper method for recursive insertion."""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
        # If data == node.data, do nothing (no duplicates)
    
    def search(self, data):
        """Search for data, return True if found."""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Helper method for recursive search."""
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def inorder_traversal(self):
        """Return inorder traversal of the tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def display(self, node=None, level=0, prefix="Root: "):
        """Display the tree structure."""
        if node is None:
            node = self.root
            if node is None:
                return "Empty Tree"
        
        result = []
        self._display_recursive(node, level, prefix, result)
        return "\n".join(result)
    
    def _display_recursive(self, node, level, prefix, result):
        """Helper method to display tree structure."""
        if node:
            result.append("  " * level + prefix + str(node.data))
            self._display_recursive(node.left, level + 1, "L--- ", result)
            self._display_recursive(node.right, level + 1, "R--- ", result)


# Test the data structures
if __name__ == "__main__":
    print("=== Linked List ===")
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    print(ll)
    print("Search 20:", ll.search(20))
    print("Search 99:", ll.search(99))
    
    print("\n=== Stack ===")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())
    
    print("\n=== Queue ===")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print("Dequeue:", queue.dequeue())
    print("Front:", queue.front())
    
    print("\n=== Binary Search Tree ===")
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    print("Inorder traversal:", bst.inorder_traversal())
    print("Search 40:", bst.search(40))
    print("Search 99:", bst.search(99))
    print("\nTree structure:")
    print(bst.display())
