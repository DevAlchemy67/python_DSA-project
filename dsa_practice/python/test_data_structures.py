"""
Tests for Data Structures
"""
import pytest
from data_structures import LinkedList, Stack, Queue, BinarySearchTree


class TestLinkedList:
    """Test cases for Linked List."""
    
    def test_empty_linked_list(self):
        """Test empty linked list."""
        ll = LinkedList()
        assert ll.is_empty()
        assert ll.display() == "Empty"
    
    def test_append(self):
        """Test append operation."""
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        assert str(ll) == "10 -> 20 -> 30"
    
    def test_prepend(self):
        """Test prepend operation."""
        ll = LinkedList()
        ll.prepend(10)
        ll.prepend(20)
        assert str(ll) == "20 -> 10"
    
    def test_delete(self):
        """Test delete operation."""
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.delete(20)
        assert str(ll) == "10 -> 30"
        
        ll.delete(10)
        assert str(ll) == "30"
        
        ll.delete(30)
        assert str(ll) == "Empty"
    
    def test_search(self):
        """Test search operation."""
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        assert ll.search(20)
        assert ll.search(10)
        assert ll.search(30)
        assert not ll.search(40)


class TestStack:
    """Test cases for Stack."""
    
    def test_empty_stack(self):
        """Test empty stack."""
        stack = Stack()
        assert stack.is_empty()
        assert stack.size() == 0
    
    def test_push_peek(self):
        """Test push and peek operations."""
        stack = Stack()
        stack.push(10)
        stack.push(20)
        assert stack.peek() == 20
        assert stack.size() == 2
    
    def test_pop(self):
        """Test pop operation."""
        stack = Stack()
        stack.push(10)
        stack.push(20)
        assert stack.pop() == 20
        assert stack.pop() == 10
        assert stack.is_empty()
    
    def test_pop_empty_stack(self):
        """Test pop from empty stack raises error."""
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()


class TestQueue:
    """Test cases for Queue."""
    
    def test_empty_queue(self):
        """Test empty queue."""
        queue = Queue()
        assert queue.is_empty()
        assert queue.size() == 0
    
    def test_enqueue_front(self):
        """Test enqueue and front operations."""
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        assert queue.front() == 10
        assert queue.size() == 2
    
    def test_dequeue(self):
        """Test dequeue operation."""
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        assert queue.dequeue() == 10
        assert queue.dequeue() == 20
        assert queue.is_empty()
    
    def test_dequeue_empty_queue(self):
        """Test dequeue from empty queue raises error."""
        queue = Queue()
        with pytest.raises(IndexError):
            queue.dequeue()


class TestBinarySearchTree:
    """Test cases for Binary Search Tree."""
    
    def test_empty_bst(self):
        """Test empty BST."""
        bst = BinarySearchTree()
        assert bst.root is None
        assert not bst.search(5)
    
    def test_insert(self):
        """Test insert operation."""
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(30)
        bst.insert(70)
        assert bst.search(50)
        assert bst.search(30)
        assert bst.search(70)
        assert not bst.search(40)
    
    def test_search(self):
        """Test search operation."""
        bst = BinarySearchTree()
        for val in [50, 30, 70, 20, 40, 60, 80]:
            bst.insert(val)
        
        assert bst.search(50)
        assert bst.search(20)
        assert bst.search(80)
        assert not bst.search(25)
        assert not bst.search(90)
    
    def test_inorder_traversal(self):
        """Test inorder traversal returns sorted elements."""
        bst = BinarySearchTree()
        for val in [50, 30, 70, 20, 40, 60, 80]:
            bst.insert(val)
        
        traversal = bst.inorder_traversal()
        assert traversal == [20, 30, 40, 50, 60, 70, 80]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
