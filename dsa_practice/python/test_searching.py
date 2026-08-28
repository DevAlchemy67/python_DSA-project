"""
Tests for Searching Algorithms
"""
import pytest
from searching import linear_search, binary_search, binary_search_recursive


class TestSearching:
    """Test cases for searching algorithms."""
    
    def test_linear_search_found(self):
        """Test linear search when element is present."""
        arr = [1, 2, 3, 4, 5]
        assert linear_search(arr, 3) == 2
        assert linear_search(arr, 1) == 0
        assert linear_search(arr, 5) == 4
    
    def test_linear_search_not_found(self):
        """Test linear search when element is not present."""
        arr = [1, 2, 3, 4, 5]
        assert linear_search(arr, 6) == -1
        assert linear_search(arr, 0) == -1
    
    def test_linear_search_empty_array(self):
        """Test linear search on empty array."""
        assert linear_search([], 5) == -1
    
    def test_binary_search_found(self):
        """Test binary search when element is present."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert binary_search(arr, 1) == 0
        assert binary_search(arr, 5) == 4
        assert binary_search(arr, 10) == 9
        assert binary_search(arr, 3) == 2
    
    def test_binary_search_not_found(self):
        """Test binary search when element is not present."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert binary_search(arr, 0) == -1
        assert binary_search(arr, 11) == -1
        assert binary_search(arr, 5.5) == -1
    
    def test_binary_search_empty_array(self):
        """Test binary search on empty array."""
        assert binary_search([], 5) == -1
    
    def test_binary_search_recursive_found(self):
        """Test recursive binary search when element is present."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert binary_search_recursive(arr, 1) == 0
        assert binary_search_recursive(arr, 5) == 4
        assert binary_search_recursive(arr, 10) == 9
    
    def test_binary_search_recursive_not_found(self):
        """Test recursive binary search when element is not present."""
        arr = [1, 2, 3, 4, 5]
        assert binary_search_recursive(arr, 0) == -1
        assert binary_search_recursive(arr, 6) == -1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
