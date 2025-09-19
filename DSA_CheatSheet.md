# 📘 DSA Quick Notes

---

## ⏱️ Time Complexities

| Complexity | Example |
|------------|---------------------------------------------|
| O(1)       | Access by index in array, push/pop in stack |
| O(log n)   | Binary search, heap insert/delete           |
| O(n)       | Linear search, traversing array             |
| O(n log n) | Merge sort, heap sort, quick sort (avg)     |
| O(n²)      | Bubble/Insertion/Selection sort             |
| O(2^n)     | Recursion (subset generation, naive DP)     |
| O(n!)      | Traveling salesman brute force              |

---

## 📂 Data Structures

| Data Structure       | Access | Search | Insert | Delete |
|----------------------|--------|--------|--------|--------|
| Array                | O(1)   | O(n)   | O(n)   | O(n)   |
| Stack                | O(n)   | O(n)   | O(1)   | O(1)   |
| Queue                | O(n)   | O(n)   | O(1)   | O(1)   |
| Singly Linked List   | O(n)   | O(n)   | O(1)   | O(1)   |
| Doubly Linked List   | O(n)   | O(n)   | O(1)   | O(1)   |
| Hash Table           | –      | O(1)   | O(1)   | O(1)   |
| BST (avg)            | O(log n) | O(log n) | O(log n) | O(log n) |
| BST (worst, skewed)  | O(n)   | O(n)   | O(n)   | O(n)   |
| Balanced BST (AVL, RB)| O(log n) | O(log n) | O(log n) | O(log n) |
| Heap                 | –      | O(n)   | O(log n) | O(log n) |

---

## ⚡ Sorting Algorithms

| Algorithm      | Time (Best) | Time (Avg) | Time (Worst) | Space   | Notes |
|----------------|-------------|------------|--------------|---------|-------|
| QuickSort      | O(n log n)  | O(n log n) | O(n²)        | O(log n) | Fast, in-place, cache-friendly; bad worst-case unless randomized. Divide with pivot. |
| MergeSort      | O(n log n)  | O(n log n) | O(n log n)   | O(n)    | Always safe; good for linked lists; stable. |
| HeapSort       | O(n log n)  | O(n log n) | O(n log n)   | O(1)    | In-place; not stable; slower in practice than QuickSort. |
| Insertion Sort | O(n)        | O(n²)      | O(n²)        | O(1)    | Good for nearly sorted/small arrays. |
| Selection Sort | O(n²)       | O(n²)      | O(n²)        | O(1)    | Rarely used; simple; least swaps. |
| Bubble Sort    | O(n)        | O(n²)      | O(n²)        | O(1)    | Only for teaching, not interviews. |
| Counting Sort  | O(n + k)    | O(n + k)   | O(n + k)     | O(k)    | Only for small integer ranges. |
| Radix Sort     | O(nk)       | O(nk)      | O(nk)        | O(n+k)  | Works for integers/strings with bounded digits. |

---

## 🌳 Tree Traversals

| Traversal Type | Order               | Typical Use |
|----------------|---------------------|-------------|
| Inorder        | Left → Root → Right | BST gives sorted order |
| Preorder       | Root → Left → Right | Copying tree, expression trees |
| Postorder      | Left → Right → Root | Delete tree, postfix expressions |
| Level-order    | BFS style           | Shortest path in unweighted |

---

## 🔄 Graph Traversals

| Traversal | Data Structure Used | Time Complexity | Notes |
|-----------|---------------------|-----------------|-------|
| BFS       | Queue               | O(V + E)        | Level-order, shortest path in unweighted graph |
| DFS       | Stack / Recursion   | O(V + E)        | Depth-first, detects cycles, topological sort |

---

## 🗺️ Graph Algorithms

| Algorithm        | Complexity   | Use Case |
|------------------|-------------|----------|
| Dijkstra         | O(E log V)  | Shortest path (weighted, non-negative) |
| Bellman-Ford     | O(VE)       | Shortest path (with negatives) |
| Floyd-Warshall   | O(V³)       | All-pairs shortest path |
| Kruskal’s        | O(E log V)  | Minimum spanning tree |
| Prim’s           | O(E log V)  | Minimum spanning tree |
| Topological Sort | O(V+E)      | Scheduling, ordering |

---

## 🌲 BST vs Heap

| Aspect         | BST (Binary Search Tree)            | Heap (Binary Heap) |
|----------------|-------------------------------------|--------------------|
| Ordering       | Left < Root < Right                 | Parent ≥ children (Max) / ≤ (Min) |
| Shape          | May be skewed                       | Always complete binary tree |
| Best for       | Searching, sorted operations        | Priority queue, heap sort |
| Search         | O(log n) average, O(n) worst        | O(n) |
| Insert/Delete  | O(log n) avg (if balanced)          | O(log n) |
| Find min/max   | O(h)                                | O(1) |
| Min/Max access | Need to traverse left/right subtree | Always root |

---

## ⏳ Heap vs Priority Queue

| Aspect       | Heap                                | Priority Queue |
|--------------|-------------------------------------|----------------|
| Definition   | A complete binary tree with heap property | Abstract data type that serves elements by priority |
| Implementation | Usually binary heap (array)       | Can be built using heap, list, tree |
| Min/Max      | O(1)                                | O(1) (if heap-backed) |
| Insert/Delete| O(log n)                            | O(log n) |
| Use cases    | Heap sort, PQ implementation        | Scheduling, graph algorithms (Dijkstra, Prim) |

---

## 🌳 Special Trees

| Structure      | Properties            | Use Case |
|----------------|-----------------------|----------|
| AVL Tree       | Self-balancing BST    | Search, insert, delete in O(log n) |
| Red-Black Tree | Balanced BST (looser than AVL) | Used in STL/Java TreeMap |
| Trie           | Prefix tree           | Autocomplete, word search |
| Segment Tree   | O(log n) queries/updates | Range sum/min/max queries |
| Fenwick Tree   | O(log n) queries/updates | Range sums |

---

## 🔑 Hashing

| Aspect             | Explanation / Notes |
|--------------------|---------------------|
| Hash Table         | Data structure storing key–value pairs using a hash function. |
| Hash Map           | Implementation of a hash table (Java `HashMap`, C++ `unordered_map`, Python `dict`). |
| Hash Set           | Stores only unique keys. Backed by a hash map internally. |
| Collision Resolution | - **Chaining**: Each bucket stores a list of items. <br> - **Open Addressing**: Find next available slot (linear probing, quadratic probing, double hashing). |
| Common Uses        | - Frequency maps <br> - Prefix sums <br> - 2-sum problem <br> - Detecting duplicates |

---

## 💡 Core Concepts

| Concept        | Example |
|----------------|---------|
| Sliding Window | Longest substring without repeating |
| Two Pointers   | 2-sum in sorted array |
| Union-Find (DSU) | Cycle detection, Kruskal’s |
| Backtracking   | N-Queens, Sudoku solver |
| Greedy         | Activity selection, Huffman coding |
| Bit Manipulation | Subset generation, parity check |
| String Algorithms | KMP, Rabin-Karp, Z-algorithm |

---

## 🧮 Dynamic Programming (DP)

| Concept / Problem Type | Example Problems |
|-------------------------|------------------|
| Fibonacci (top-down vs bottom-up) | DP basics |
| 0/1 Knapsack           | Subset problems |
| Longest Common Subsequence (LCS) | String DP |
| Matrix DP              | Min path sum, unique paths |
| DP on subsequences     | LIS, Partition equal subset sum |

---

## 🐍 Python List Slicing

| Slice      | Meaning |
|------------|---------|
| `nums[i:j]` | From index `i` to `j-1` |
| `nums[i:]`  | From index `i` to end |
| `nums[:j]`  | From start to `j-1` |
| `nums[:]`   | Whole list |
| `nums[::k]` | Every k-th element |
| `nums[::-1]`| Reverse list |
| `nums[-i:]` | Last i elements |
| `nums[:-i]` | Everything except last i elements |

---
