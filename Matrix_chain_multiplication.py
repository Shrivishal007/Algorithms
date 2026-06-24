"""
Problem: Matrix Chain Multiplication. Find the most efficient way to multiply a sequence of matrices.
Approach: Bottom-up Dynamic Programming.
Assumptions: The input array 'p' represents dimensions such that matrix A_i has dimension p[i-1] x p[i].
Input: An array 'p' of integers representing the matrix chain dimensions.
Output: DP table 'm' (minimum scalar multiplications), split table 's', and the optimal parenthesization printed.
Time Complexity: O(n^3), where n is the number of matrices (len(p) - 1).
Space Complexity: O(n^2) to store the 'm' and 's' 2D arrays.
Key Idea: 
dp[i][j] = min over all k in [i, j-1] of:
    dp[i][k] + dp[k+1][j] + (p[i-1] * p[k] * p[j])
Base case:
dp[i][i] = 0
"""

def matrixChainOrder(p):
    n = len(p) - 1

    # m[i][j] stores the minimum number of scalar multiplications needed to compute matrix A_i..A_j
    m = [[0] * (n + 1) for _ in range(n + 1)]
    # s[i][j] stores the index k which achieved the optimal split for A_i..A_j
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # l is the chain length (starts at 2, up to n)
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')

            print(f"\nm[{i}][{j}]:")
            q_vals = []

            # k is the split point between i and j-1
            for k in range(i, j):
                # q = scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

                print(f"\tk = {k}, q = m[{i}][{k}] + m[{k + 1}][{j}] + (p[{i - 1}] * p[{k}] * p[{j}])")
                print(f"\t\t = {m[i][k]} + {m[k + 1][j]} + ({p[i - 1]} * {p[k]} * {p[j]}) = {q}")

                q_vals.append(q)

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

            print(f"min{tuple(q_vals)} = {min(q_vals)}")
    print()

    return m, s

def printOptimalParens(s, i, j):
    # Base case: a single matrix
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        printOptimalParens(s, i, s[i][j])       # Recursively format left subchain
        print(" * ", end="")
        printOptimalParens(s, s[i][j] + 1, j)   # Recursively format right subchain
        print(")", end="")

if __name__ == "__main__":
    p = list(map(int, input("Enter the order values: ").split()))
    n = len(p) - 1

    m, s = matrixChainOrder(p)

    # Print M Table
    for j in range(n + 1):
        if j < 1:
            print(" ", end="")
        else:
            print(f"{j:8}", end="")
    print()
    for i in range(1, n + 1):
        print(i, end="")

        for j in range(1, n + 1):
            if i <= j:
                print(f"{m[i][j]:8}", end="")
            else:
                print(f"{'-':>8}", end="")
        print()
    print()

    # Print S Table
    for j in range(n + 1):
        if j < 1:
            print(" ", end="")
        else:
            print(f"{j:8}", end="")
    print()
    for i in range(1, n + 1):
        print(i, end="")

        for j in range(1, n + 1):
            if i < j:
                print(f"{s[i][j]:8}", end="")
            else:
                print(f"{'-':>8}", end="")
        print()
    print()

    print("Expression:", end=" ")
    printOptimalParens(s, 1, n)