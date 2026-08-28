/**
 * Searching Algorithms Implementation for DSA Practice in C++
 */

#include <iostream>
#include <vector>

using namespace std;

// Linear Search: O(n) time complexity
int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

// Binary Search (Iterative): O(log n) time complexity
int binarySearch(const vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

// Binary Search (Recursive): O(log n) time complexity
int binarySearchRecursive(const vector<int>& arr, int target, int low, int high) {
    if (low > high) {
        return -1;
    }
    
    int mid = low + (high - low) / 2;
    
    if (arr[mid] == target) {
        return mid;
    } else if (arr[mid] < target) {
        return binarySearchRecursive(arr, target, mid + 1, high);
    } else {
        return binarySearchRecursive(arr, target, low, mid - 1);
    }
}

// Wrapper for recursive binary search
int binarySearchRecursive(const vector<int>& arr, int target) {
    return binarySearchRecursive(arr, target, 0, arr.size() - 1);
}

int main() {
    vector<int> sorted_data = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int target = 23;
    
    cout << "Sorted array: ";
    for (int num : sorted_data) {
        cout << num << " ";
    }
    cout << endl;
    
    cout << "\nSearching for " << target << ":" << endl;
    cout << "Linear Search: " << linearSearch(sorted_data, target) << endl;
    cout << "Binary Search (iterative): " << binarySearch(sorted_data, target) << endl;
    cout << "Binary Search (recursive): " << binarySearchRecursive(sorted_data, target) << endl;
    
    int not_found = 100;
    cout << "\nSearching for " << not_found << " (not in array):" << endl;
    cout << "Linear Search: " << linearSearch(sorted_data, not_found) << endl;
    cout << "Binary Search: " << binarySearch(sorted_data, not_found) << endl;
    
    return 0;
}
