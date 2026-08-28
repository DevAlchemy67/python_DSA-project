# Python DSA Practice

This folder contains Python implementations of common Data Structures and Algorithms for practice.

## Available Implementations

### Sorting Algorithms
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

### Searching Algorithms
- Linear Search
- Binary Search

### Data Structures
- Linked List
- Stack
- Queue
- Binary Search Tree

## How to Use

1. Import and use the implementations:
```python
from sorting import bubble_sort, quick_sort
from data_structures import LinkedList, Stack

arr = [5, 2, 9, 1, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)
```

2. Run tests:
```bash
python -m pytest test_*.py -v
```
