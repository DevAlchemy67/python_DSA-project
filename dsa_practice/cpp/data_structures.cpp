/**
 * Data Structures Implementation for DSA Practice in C++
 */

#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

// Node class for linked structures
class Node {
public:
    int data;
    Node* next;
    
    Node(int data) : data(data), next(nullptr) {}
};

// Linked List class
class LinkedList {
private:
    Node* head;
public:
    LinkedList() : head(nullptr) {}
    
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
    
    bool isEmpty() const {
        return head == nullptr;
    }
    
    void append(int data) {
        Node* newNode = new Node(data);
        if (head == nullptr) {
            head = newNode;
            return;
        }
        
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
    }
    
    void prepend(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }
    
    void remove(int data) {
        if (head == nullptr) return;
        
        if (head->data == data) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        
        Node* current = head;
        while (current->next != nullptr) {
            if (current->next->data == data) {
                Node* temp = current->next;
                current->next = current->next->next;
                delete temp;
                return;
            }
            current = current->next;
        }
    }
    
    bool search(int data) const {
        Node* current = head;
        while (current != nullptr) {
            if (current->data == data) {
                return true;
            }
            current = current->next;
        }
        return false;
    }
    
    void display() const {
        Node* current = head;
        if (current == nullptr) {
            cout << "Empty";
            return;
        }
        
        while (current != nullptr) {
            cout << current->data;
            if (current->next != nullptr) {
                cout << " -> ";
            }
            current = current->next;
        }
    }
};

// Stack class
class Stack {
private:
    vector<int> items;
public:
    bool isEmpty() const {
        return items.empty();
    }
    
    void push(int item) {
        items.push_back(item);
    }
    
    int pop() {
        if (isEmpty()) {
            throw out_of_range("Pop from empty stack");
        }
        int top = items.back();
        items.pop_back();
        return top;
    }
    
    int peek() const {
        if (isEmpty()) {
            throw out_of_range("Peek from empty stack");
        }
        return items.back();
    }
    
    int size() const {
        return items.size();
    }
    
    void display() const {
        cout << "[ ";
        for (size_t i = 0; i < items.size(); i++) {
            cout << items[i];
            if (i < items.size() - 1) {
                cout << ", ";
            }
        }
        cout << " ]";
    }
};

// Queue class
class Queue {
private:
    vector<int> items;
public:
    bool isEmpty() const {
        return items.empty();
    }
    
    void enqueue(int item) {
        items.push_back(item);
    }
    
    int dequeue() {
        if (isEmpty()) {
            throw out_of_range("Dequeue from empty queue");
        }
        int front = items.front();
        items.erase(items.begin());
        return front;
    }
    
    int front() const {
        if (isEmpty()) {
            throw out_of_range("Front from empty queue");
        }
        return items.front();
    }
    
    int size() const {
        return items.size();
    }
    
    void display() const {
        cout << "[ ";
        for (size_t i = 0; i < items.size(); i++) {
            cout << items[i];
            if (i < items.size() - 1) {
                cout << ", ";
            }
        }
        cout << " ]";
    }
};

// Tree Node for BST
class TreeNode {
public:
    int data;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(int data) : data(data), left(nullptr), right(nullptr) {}
};

// Binary Search Tree class
class BinarySearchTree {
private:
    TreeNode* root;
    
    TreeNode* insertRecursive(TreeNode* node, int data) {
        if (node == nullptr) {
            return new TreeNode(data);
        }
        
        if (data < node->data) {
            node->left = insertRecursive(node->left, data);
        } else if (data > node->data) {
            node->right = insertRecursive(node->right, data);
        }
        // If data == node->data, do nothing (no duplicates)
        
        return node;
    }
    
    bool searchRecursive(TreeNode* node, int data) const {
        if (node == nullptr) {
            return false;
        }
        
        if (node->data == data) {
            return true;
        } else if (data < node->data) {
            return searchRecursive(node->left, data);
        } else {
            return searchRecursive(node->right, data);
        }
    }
    
    void inorderRecursive(TreeNode* node, vector<int>& result) const {
        if (node != nullptr) {
            inorderRecursive(node->left, result);
            result.push_back(node->data);
            inorderRecursive(node->right, result);
        }
    }
    
    void displayRecursive(TreeNode* node, int level, const string& prefix) const {
        if (node != nullptr) {
            cout << string(level * 2, ' ') << prefix << node->data << endl;
            displayRecursive(node->left, level + 1, "L--- ");
            displayRecursive(node->right, level + 1, "R--- ");
        }
    }
    
    void deleteTree(TreeNode* node) {
        if (node != nullptr) {
            deleteTree(node->left);
            deleteTree(node->right);
            delete node;
        }
    }
public:
    BinarySearchTree() : root(nullptr) {}
    
    ~BinarySearchTree() {
        deleteTree(root);
    }
    
    void insert(int data) {
        root = insertRecursive(root, data);
    }
    
    bool search(int data) const {
        return searchRecursive(root, data);
    }
    
    vector<int> inorderTraversal() const {
        vector<int> result;
        inorderRecursive(root, result);
        return result;
    }
    
    void display() const {
        if (root == nullptr) {
            cout << "Empty Tree" << endl;
            return;
        }
        displayRecursive(root, 0, "Root: ");
    }
};

int main() {
    cout << "=== Linked List ===" << endl;
    LinkedList ll;
    ll.append(10);
    ll.append(20);
    ll.prepend(5);
    ll.display();
    cout << endl;
    cout << "Search 20: " << (ll.search(20) ? "Found" : "Not Found") << endl;
    cout << "Search 99: " << (ll.search(99) ? "Found" : "Not Found") << endl;
    
    cout << "\n=== Stack ===" << endl;
    Stack stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.display();
    cout << endl;
    cout << "Pop: " << stack.pop() << endl;
    cout << "Peek: " << stack.peek() << endl;
    
    cout << "\n=== Queue ===" << endl;
    Queue queue;
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.display();
    cout << endl;
    cout << "Dequeue: " << queue.dequeue() << endl;
    cout << "Front: " << queue.front() << endl;
    
    cout << "\n=== Binary Search Tree ===" << endl;
    BinarySearchTree bst;
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    for (int val : values) {
        bst.insert(val);
    }
    vector<int> traversal = bst.inorderTraversal();
    cout << "Inorder traversal: ";
    for (int val : traversal) {
        cout << val << " ";
    }
    cout << endl;
    cout << "Search 40: " << (bst.search(40) ? "Found" : "Not Found") << endl;
    cout << "Search 99: " << (bst.search(99) ? "Found" : "Not Found") << endl;
    cout << "\nTree structure:" << endl;
    bst.display();
    
    return 0;
}
