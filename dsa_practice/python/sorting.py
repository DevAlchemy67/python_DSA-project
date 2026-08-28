"""
Sorting Algorithms Implementation for DSA Practice
"""

def bubble_sort(arr):
    """
    Bubble Sort: O(n^2) time complexity
    Repeatedly steps through the list, compares adjacent elements and swaps them if they are in wrong order.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """
    Selection Sort: O(n^2) time complexity
    Selects the smallest element from unsorted portion and swaps it with the first unsorted element.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """
    Insertion Sort: O(n^2) time complexity, O(n) for nearly sorted
    Builds the sorted array one element at a time by inserting each element in its correct position.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Merge Sort: O(n log n) time complexity
    Divide and conquer algorithm that divides the array in half, sorts each half, and merges them.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left, right):
    """Helper function to merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr, low=0, high=None):
    """
    Quick Sort: O(n log n) average, O(n^2) worst case
    Divide and conquer algorithm that selects a pivot and partitions the array.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = _partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr


def _partition(arr, low, high):
    """Helper function to partition the array for quick sort."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Test the sorting algorithms
if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_data)
    
    print("\nBubble Sort:", bubble_sort(test_data.copy()))
    print("Selection Sort:", selection_sort(test_data.copy()))
    print("Insertion Sort:", insertion_sort(test_data.copy()))
    print("Merge Sort:", merge_sort(test_data.copy()))
    print("Quick Sort:", quick_sort(test_data.copy()))
