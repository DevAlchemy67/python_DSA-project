"""
Searching Algorithms Implementation for DSA Practice
"""

def linear_search(arr, target):
    """
    Linear Search: O(n) time complexity
    Sequentially checks each element of the list until a match is found.
    Returns the index of the target if found, otherwise -1.
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Binary Search: O(log n) time complexity
    Works on sorted arrays. Repeatedly divides the search interval in half.
    Returns the index of the target if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    """
    Recursive Binary Search: O(log n) time complexity
    Recursive implementation of binary search.
    """
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# Test the searching algorithms
if __name__ == "__main__":
    sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    
    print("Sorted array:", sorted_data)
    print(f"\nSearching for {target}:")
    print("Linear Search:", linear_search(sorted_data, target))
    print("Binary Search (iterative):", binary_search(sorted_data, target))
    print("Binary Search (recursive):", binary_search_recursive(sorted_data, target))
    
    not_found = 100
    print(f"\nSearching for {not_found} (not in array):")
    print("Linear Search:", linear_search(sorted_data, not_found))
    print("Binary Search:", binary_search(sorted_data, not_found))
