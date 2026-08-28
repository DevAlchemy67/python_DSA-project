/**
 * Sorting Algorithms Implementation for DSA Practice in C++
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to print an array
void printArray(const vector<int>& arr) {
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

// Bubble Sort: O(n^2) time complexity
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

// Selection Sort: O(n^2) time complexity
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        swap(arr[i], arr[min_idx]);
    }
}

// Insertion Sort: O(n^2) time complexity, O(n) for nearly sorted
void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && key < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Merge function for Merge Sort
void merge(vector<int>& arr, int low, int mid, int high) {
    int n1 = mid - low + 1;
    int n2 = high - mid;
    
    vector<int> left(n1), right(n2);
    
    for (int i = 0; i < n1; i++)
        left[i] = arr[low + i];
    for (int j = 0; j < n2; j++)
        right[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = low;
    while (i < n1 && j < n2) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }
    
    while (i < n1) {
        arr[k] = left[i];
        i++;
        k++;
    }
    
    while (j < n2) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

// Merge Sort: O(n log n) time complexity
void mergeSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int mid = low + (high - low) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}

// Partition function for Quick Sort
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Quick Sort: O(n log n) average, O(n^2) worst case
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot_idx = partition(arr, low, high);
        quickSort(arr, low, pivot_idx - 1);
        quickSort(arr, pivot_idx + 1, high);
    }
}

// Wrapper functions for easier use
void mergeSort(vector<int>& arr) {
    mergeSort(arr, 0, arr.size() - 1);
}

void quickSort(vector<int>& arr) {
    quickSort(arr, 0, arr.size() - 1);
}

int main() {
    vector<int> test_data = {64, 34, 25, 12, 22, 11, 90};
    
    cout << "Original array: ";
    printArray(test_data);
    
    vector<int> temp = test_data;
    bubbleSort(temp);
    cout << "\nBubble Sort: ";
    printArray(temp);
    
    temp = test_data;
    selectionSort(temp);
    cout << "Selection Sort: ";
    printArray(temp);
    
    temp = test_data;
    insertionSort(temp);
    cout << "Insertion Sort: ";
    printArray(temp);
    
    temp = test_data;
    mergeSort(temp);
    cout << "Merge Sort: ";
    printArray(temp);
    
    temp = test_data;
    quickSort(temp);
    cout << "Quick Sort: ";
    printArray(temp);
    
    return 0;
}
