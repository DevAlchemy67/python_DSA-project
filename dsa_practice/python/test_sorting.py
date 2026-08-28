"""
Tests for Sorting Algorithms
"""
import pytest
from sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort


class TestSorting:
    """Test cases for sorting algorithms."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        assert bubble_sort([]) == []
        assert selection_sort([]) == []
        assert insertion_sort([]) == []
        assert merge_sort([]) == []
        assert quick_sort([]) == []
    
    def test_single_element(self):
        """Test sorting an array with one element."""
        assert bubble_sort([5]) == [5]
        assert selection_sort([5]) == [5]
        assert insertion_sort([5]) == [5]
        assert merge_sort([5]) == [5]
        assert quick_sort([5]) == [5]
    
    def test_sorted_array(self):
        """Test sorting an already sorted array."""
        arr = [1, 2, 3, 4, 5]
        assert bubble_sort(arr.copy()) == arr
        assert selection_sort(arr.copy()) == arr
        assert insertion_sort(arr.copy()) == arr
        assert merge_sort(arr.copy()) == arr
        assert quick_sort(arr.copy()) == arr
    
    def test_reverse_sorted_array(self):
        """Test sorting a reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        sorted_arr = [1, 2, 3, 4, 5]
        assert bubble_sort(arr.copy()) == sorted_arr
        assert selection_sort(arr.copy()) == sorted_arr
        assert insertion_sort(arr.copy()) == sorted_arr
        assert merge_sort(arr.copy()) == sorted_arr
        assert quick_sort(arr.copy()) == sorted_arr
    
    def test_random_array(self):
        """Test sorting a random array."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = [11, 12, 22, 25, 34, 64, 90]
        assert bubble_sort(arr.copy()) == sorted_arr
        assert selection_sort(arr.copy()) == sorted_arr
        assert insertion_sort(arr.copy()) == sorted_arr
        assert merge_sort(arr.copy()) == sorted_arr
        assert quick_sort(arr.copy()) == sorted_arr
    
    def test_array_with_duplicates(self):
        """Test sorting an array with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        assert bubble_sort(arr.copy()) == sorted_arr
        assert selection_sort(arr.copy()) == sorted_arr
        assert insertion_sort(arr.copy()) == sorted_arr
        assert merge_sort(arr.copy()) == sorted_arr
        assert quick_sort(arr.copy()) == sorted_arr


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
