# DSA Practice Projects

This folder contains complete implementations of common Data Structures and Algorithms in **Python** and **C++** for practice and learning.

## Structure

```
dsa_practice/
├── python/
│   ├── sorting.py          # Sorting algorithms
│   ├── searching.py        # Searching algorithms
│   ├── data_structures.py # Data structures
│   ├── test_sorting.py     # Tests for sorting
│   ├── test_searching.py   # Tests for searching
│   └── test_data_structures.py # Tests for data structures
└── cpp/
    ├── sorting.cpp         # Sorting algorithms
    ├── searching.cpp       # Searching algorithms
    └── data_structures.cpp # Data structures
```

## Python Implementations

### Sorting Algorithms (`python/sorting.py`)
- **Bubble Sort** - O(n²) - Simple comparison-based sort
- **Selection Sort** - O(n²) - Selects minimum and swaps
- **Insertion Sort** - O(n²), O(n) for nearly sorted - Builds sorted array one element at a time
- **Merge Sort** - O(n log n) - Divide and conquer with merging
- **Quick Sort** - O(n log n) average, O(n²) worst - Divide and conquer with pivot

### Searching Algorithms (`python/searching.py`)
- **Linear Search** - O(n) - Sequential search through array
- **Binary Search (Iterative)** - O(log n) - Works on sorted arrays
- **Binary Search (Recursive)** - O(log n) - Recursive implementation

### Data Structures (`python/data_structures.py`)
- **Linked List** - O(1) insertion/deletion at head, O(n) at tail
- **Stack** - LIFO (Last In First Out) - O(1) push/pop/peek
- **Queue** - FIFO (First In First Out) - O(1) enqueue/dequeue
- **Binary Search Tree** - O(log n) average for operations

### Running Python Tests
```bash
cd dsa_practice/python
python -m pytest test_*.py -v
```

Or run individual test files:
```bash
python test_sorting.py
python test_searching.py
python test_data_structures.py
```

## C++ Implementations

### Sorting Algorithms (`cpp/sorting.cpp`)
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

### Searching Algorithms (`cpp/searching.cpp`)
- Linear Search
- Binary Search (Iterative)
- Binary Search (Recursive)

### Data Structures (`cpp/data_structures.cpp`)
- Linked List
- Stack
- Queue
- Binary Search Tree

### Compiling and Running C++

Compile individual files:
```bash
cd dsa_practice/cpp
g++ -std=c++11 sorting.cpp -o sorting
./sorting
```

Or compile all at once:
```bash
g++ -std=c++11 *.cpp -o dsa_demo
./dsa_demo
```

## Usage Examples

### Python
```python
from sorting import quick_sort, merge_sort
from searching import binary_search
from data_structures import LinkedList, Stack, Queue, BinarySearchTree

# Sorting
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = quick_sort(arr.copy())
print(sorted_arr)  # [1, 2, 5, 5, 6, 9]

# Searching
sorted_data = [1, 2, 5, 6, 9]
idx = binary_search(sorted_data, 5)
print(idx)  # 2

# Data Structures
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
print(ll)  # 5 -> 10 -> 20

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # 1

bst = BinarySearchTree()
for val in [50, 30, 70, 20, 40]:
    bst.insert(val)
print(bst.search(40))  # True
```

### C++
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Include the implementations
void quickSort(vector<int>& arr);
int binarySearch(const vector<int>& arr, int target);

int main() {
    vector<int> arr = {5, 2, 9, 1, 5, 6};
    
    quickSort(arr);
    for (int num : arr) {
        cout << num << " ";  // 1 2 5 5 6 9
    }
    
    int idx = binarySearch(arr, 5);
    cout << idx;  // 2
    
    return 0;
}
```

## Suggested Practice Topics

### Additional Sorting Algorithms to Implement
- Heap Sort
- Counting Sort
- Radix Sort
- Bucket Sort
- Shell Sort

### Additional Searching Algorithms
- Jump Search
- Interpolation Search
- Exponential Search

### Additional Data Structures
- Doubly Linked List
- Circular Linked List
- Priority Queue (Heap)
- AVL Tree
- Red-Black Tree
- Hash Table
- Graph (Adjacency List/Matrix)

### Advanced Topics
- Dynamic Programming (Fibonacci, Knapsack, LCS)
- Graph Algorithms (DFS, BFS, Dijkstra, Prim, Kruskal)
- Divide and Conquer
- Greedy Algorithms
- Backtracking
