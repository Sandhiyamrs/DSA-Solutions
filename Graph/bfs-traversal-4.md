# 🌐 BFS Traversal of Graph

## 📝 Problem Statement
Given a graph represented as an adjacency list and a starting node `s`, return the **Breadth-First Search (BFS)** traversal of the graph.

## 🧪 Example
Input: graph = {0:[1,2], 1:[0,3], 2:[0,4], 3:[1], 4:[2]}, start = 0  
Output: [0,1,2,3,4]  

### Explanation:
Start from node 0 → visit neighbors 1,2 → visit their neighbors → final BFS order [0,1,2,3,4]

## ✔️ Constraints
- Graph nodes are labeled from 0 to n-1
- Graph is connected or disconnected
