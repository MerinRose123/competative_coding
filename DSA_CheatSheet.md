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

| **Category**                    | **Problem Type / Example**                                                  | **DP Dimensions**                   | **Key Recurrence / Idea**                                                  | **Notes / Tips**                                                |
| --------------------------------| --------------------------------------------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **1D Array / Sequence**         | House Robber (198), Maximum Subarray (53), Climbing Stairs (70)             | `dp[i]`                             | `dp[i] = max(dp[i-1], dp[i-2]+nums[i])`                                    | Typical prefix/subsequence problems; often 1D DP               |
| **2D Grid / Matrix**            | Unique Paths (62), Minimum Path Sum (64), Dungeon Game (174)                | `dp[i][j]`                          | `dp[i][j] = f(dp[i-1][j], dp[i][j-1])`                                     | Grid traversal; can often be optimized to 1D row               |
| **Knapsack / Subset**           | 0/1 Knapsack (416, 474), Coin Change (322, 518)                             | `dp[i][w]` or `dp[w]`               | `dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])`              | Classic decision DP; can optimize space to 1D                  |
| **Strings**                     | LCS (1143), Edit Distance (72), Word Break (139)                            | `dp[i][j]` or `dp[i]`               | `dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`                       | Subsequence vs substring; segmentation; pattern matching       |
| **Subsequence Counting**        | Distinct Subsequences (115), Decode Ways (91)                               | `dp[i]` or `dp[i][j]`               | `dp[i] = sum of valid previous splits`                                     | Count ways instead of max/min                                  |
| **Palindromes**                 | Longest Palindromic Substring (5), Subsequence (516), Min insertions (1312) | `dp[i][j]`                          | `dp[i][j] = dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1])` | Often 2D DP; can sometimes optimize to 1D diagonals            |
| **Interval / Range**            | Matrix Chain Multiplication (312), Burst Balloons (312)                     | `dp[i][j]`                          | `dp[i][j] = min/max(dp[i][k] + dp[k+1][j] + cost[i][j])`                   | Usually for ranges or partitions                               |
| **Bitmask / Subset**            | Traveling Salesman (TSP), Shortest Superstring                              | `dp[mask][i]`                       | `dp[mask][i] = min(dp[mask ^ (1<<i)][j] + cost[j][i])`                     | Used for small N; combinatorial DP                             |
| **Tree DP**                     | Maximum Path Sum (124), House Robber III (337)                              | `dfs(node)` returns tuple or values | `dp[node] = f(dp[left], dp[right])`                                        | Often post-order traversal; can handle multiple states per node|
| **Monotonic / Optimization DP** | Stock Buy/Sell (121, 188), Jump Game (45)                                   | `dp[i]`                             | `dp[i] = min/max(f(dp[j]))`                                                | Usually optimize with monotonic stack or prefix max/min        |
| **Game Theory / Minimax DP**    | Stone Game (877), Predict the Winner (486)                                  | `dp[i][j]`                          | `dp[i][j] = max(score[i]+sum-dp[i+1][j], score[j]+sum-dp[i][j-1])`         | Player vs player; usually two-player optimal game              |
| **Sliding Window + DP**         | Longest Substring with K Distinct (159)                                     | `dp[i]` or window                   | Maintain valid count while expanding window                                | Sometimes hybrid DP + sliding window                           |

---

# String Problem Strategy Cheat Sheet

| Pattern / Keywords | Typical Approach | Why / Description | Example Problem |
|-------------------------|----------------------|----------------------|----------------------|
| Check subsequence (order matters, not contiguous) | Two pointers | You just scan through both strings once (`s` pointer moves when chars match), no need for DP | [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/) |
| Check substring (contiguous) | Sliding window / Two pointers | Efficient to maintain a window of characters and check conditions for contiguous substring | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| String formation (order not important) | Hash map / Counter / Frequency array | Only the frequency of characters matters, not order | [383. Ransom Note](https://leetcode.com/problems/ransom-note/) |
| Anagram problems | Hash map / Sorting / Frequency array | Compare character counts to group or verify anagrams | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) |
| Longest / shortest subsequence or substring | DP (LCS, subsequence DP) | Optimal substructure with overlapping subproblems — need to compare prefixes | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) |
| Minimum edits / transformations | DP (Edit distance, LCS) | Need to track minimum operations to transform one string to another | [72. Edit Distance](https://leetcode.com/problems/edit-distance/) |
| Greedy choice possible | Greedy | Problem allows local decisions to build global optimum, e.g., remove smallest character, balance parentheses | [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) |
| Prefix search, autocomplete, dictionary problems | Trie | Efficient prefix storage and lookup, fast insert/search for word patterns | [208. Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) |
| Repeating substring / pattern detection | KMP / Z-function / Rabin–Karp | Linear-time string pattern search, avoids brute-force | [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |
| Distinct substrings count | Suffix Array / Automaton / Trie | Handle large numbers of substrings efficiently | [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) |
| Palindromes | Expand around center / DP / Manacher’s algorithm | Efficient detection of palindromic substrings; DP helps with LPS; Manacher’s is O(n) | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |
| Multiple subsequence queries on same string | Preprocess + Binary Search | Precompute character positions to speed up repeated queries | [792. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) |
| Lexicographic smallest / largest substring | Greedy / Suffix Array | Problem requires comparing substrings to find min/max order efficiently | [1163. Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/) |
| Find longest prefix-suffix (borders, repetitions) | KMP prefix function / Z-function | Track repeating patterns or borders efficiently | [1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) |
| String hashing (fast substring equality) | Polynomial rolling hash | Compare substrings in O(1) time using precomputed hashes | [1316. Distinct Echo Substrings](https://leetcode.com/problems/distinct-echo-substrings/) |
| Segmented substring checks | Prefix sums / Hashing | Quickly check substring properties (like counts) in constant time | [1177. Can Make Palindrome from Substring](https://leetcode.com/problems/can-make-palindrome-from-substring/) |
| Compression / repeated pattern matching | DP / Hashing | Detect repeated structure, pattern or periodicity in strings efficiently | [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) |

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

## 📐 Geometry & Math (Common in Coding Rounds)

| Concept               | Complexity         | Notes                       |
|-----------------------|--------------------|-----------------------------|
| **GCD (Euclidean Algo)** | O(log min(a,b)) | Useful in number theory     |
| **Sieve of Eratosthenes** | O(n log log n) | Prime generation            |
| **Fast Exponentiation**  | O(log n)        | Modular power, cryptography |
| **Convex Hull (Graham / Jarvis)** | O(n log n) | Computational geometry  |

---
