# Learn Algorithms at Ease

A comprehensive collection of classic algorithms implemented in Python. This repository spans multiple domains of computer science, including Dynamic Programming, Divide and Conquer, Linear Algebra, Mathematical Optimization, and Backtracking. 

These scripts are designed for educational purposes, demonstrating core algorithmic concepts, time/space complexity trade-offs, and mathematical problem-solving.

## Features
* **Educational Focus:** Clean, heavily commented Python code.
* **Visual Outputs:** Includes step-by-step matrix rendering for DP and Simplex tableaus.
* **Mathematical Rigor:** Exact implementations of classic theorems and optimization techniques.

## Table of Contents

### Dynamic Programming
* **Edit Distance (Levenshtein Distance):** Calculates the minimum number of insertions, deletions, and substitutions required to transform one string into another, including step-by-step operation tracking.
* **0/1 Knapsack Problem:** Solves the classic resource-allocation problem to maximize profit given a strict weight capacity, including traceback to identify selected items.
* **Longest Common Subsequence (LCS):** Finds the longest subsequence common to two sequences, rendering the DP matrix and the final reconstructed string.
* **Matrix Chain Multiplication:** Determines the most efficient way to multiply a given sequence of matrices to minimize total scalar multiplications.

### Divide and Conquer
* **Karatsuba Multiplication:** A fast multiplication algorithm for large numbers that reduces the multiplication of two $n$-digit numbers from $O(n^2)$ to $O(n^{1.58})$.

### Linear Algebra & Optimization
* **LUP Decomposition:** Performs LU decomposition with partial pivoting ($PA = LU$) to solve systems of linear equations and compute matrix inverses efficiently.
* **Simplex Algorithm (Tableau Method):** Solves Linear Programming maximization problems, dynamically iterating through basic feasible solutions to find the absolute optimum.

### Backtracking & State Space Search
* **N-Queens Puzzle:** Finds all valid placements of $N$ mutually non-attacking queens on an $N \times N$ chessboard.
* **Sum of Subsets:** Utilizes branch-and-bound pruning to find all subsets of a given set whose elements sum to a highly specific target value.

## Books Referred & Resources

The implementations in this repository are guided by and modeled after the standard literature in computer science and optimization:

* **Introduction to Algorithms (CLRS)** by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
  * *Used for: LUP Decomposition, Matrix Chain Multiplication, 0/1 Knapsack, and N-Queens.*
* **Algorithm Design** by Jon Kleinberg and Éva Tardos.
  * *Used for: Sequence Alignment (Edit Distance) and Divide and Conquer paradigms.*
* **Linear Programming and Network Flows** by Mokhtar S. Bazaraa, John J. Jarvis, and Hanif D. Sherali.
  * *Used for: The Simplex Method (Tableau implementation).*

## Contribution

This repository is built for learning and continuous improvement! 

* **Found a bug or want an optimization?** Feel free to open an [Issue](https://github.com/Shrivishal007/Algorithms/issues) or submit a Pull Request.
* **Want to use it locally?** Just clone and explore
```bash
git clone https://github.com/Shrivishal007/Algorithms.git
```
Developed with 📖 and 💻 by Shrivishal.