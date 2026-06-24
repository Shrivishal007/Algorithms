"""
Problem: Solve systems of linear equations and compute matrix inverses efficiently.
Approach: LUP Decomposition (LU Decomposition with Partial Pivoting).
Assumptions: The input matrix A is a square n x n matrix.
Input: A square matrix A of size n x n, and a constant vector B of size n.
Output: L, U, and P matrices, the solution vector X for AX = B, and the inverse matrix A^-1.
Time Complexity: O(n^3) for decomposition and inverse, O(n^2) for solving a single system.
Space Complexity: O(n^2) to store the L, U, and Inverse matrices.
Key Idea: 
AX = B      where P*A = L*U
LUX = PB    where LY = PB and UX = Y
"""

def lupDecomposition(A):
    n = len(A)
    # Create a deep copy of A to work on in-place
    a = [row[:] for row in A]

    # Initialize permutation vector P to track row swaps
    P = list(range(n))

    for k in range(n - 1):
        # 1. Partial Pivoting: Find the row with the largest absolute value in current column
        pivot = abs(a[k][k])
        k_i = k

        for i in range(k, n):
            if abs(a[i][k]) > pivot:
                pivot = abs(a[i][k])
                k_i = i

        if pivot == 0:
            raise ValueError('Singular matrix')

        # Swap rows in the matrix 'a' and the permutation vector 'P'
        a[k], a[k_i] = a[k_i], a[k]
        P[k], P[k_i] = P[k_i], P[k]

        # 2. Gaussian Elimination: Eliminate entries below the pivot
        for i in range(k + 1, n):
            a[i][k] /= a[k][k] # Multiplier
            for j in range(k + 1, n):
                a[i][j] -= a[i][k] * a[k][j]

    if a[n - 1][n - 1] == 0:
        raise ValueError('Singular matrix')

    # 3. Extract L and U matrices from the combined matrix 'a'
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1 # L has 1s on the diagonal
        for j in range(i):
            L[i][j] = a[i][j]

        for j in range(i, n):
            U[i][j] = a[i][j]

    return L, U, P

def lupSolve(L, U, P, B):
    n = len(L)

    # Apply permutation to B (PB)
    PB = [0] * n
    for i in range(n):
        PB[i] = B[P[i]]

    # Forward Substitution: Solve Ly = PB
    Y = [0] * n
    for i in range(n):
        summation = 0
        for j in range(i):
            summation += L[i][j] * Y[j]
        Y[i] = PB[i] - summation

    # Backward Substitution: Solve Ux = Y
    X = [0] * n
    for i in range(n - 1, -1, -1):
        summation = 0
        for j in range(i + 1, n):
            summation += U[i][j] * X[j]
        X[i] = (Y[i] - summation) / U[i][i]

    return X

def inverse(L, U, P):
    n = len(L)
    A_inv = [[0] * n for _ in range(n)]

    # Solve the system against the identity matrix columns (basis vectors)
    for j in range(n):
        B_j = [0] * n
        B_j[j] = 1
        X_j = lupSolve(L, U, P, B_j)

        for i in range(n):
            A_inv[i][j] = X_j[i]

    return A_inv

def printMatrix(m, name):
    n = len(m)
    print(f"{name}:")
    for i in range(n):
        for j in range(n):
            print(f"{m[i][j]:8.3f}", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter order of Matrix A: "))
    A = []
    print("Enter A matrix: ")
    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        A.append(row)
    b = list(map(int, input("Enter B values: ").split()))

    print("\nEquations:")
    for i in range(n):
        for j in range(n):
            print(f"{A[i][j]:3}", end=" ")
        print(f" | x_{i + 1} | =  {b[i]}")
    print()

    try:
        L, U, P = lupDecomposition(A)

    except ValueError as e:
        print("LUP decomposition failed:", e)

    else:
        printMatrix(L, "L Matrix")
        print()
        printMatrix(U, "U Matrix")
        print()
        print("P Matrix:")
        for i in range(n):
            for j in range(n):
                print(1 if P[i] == j else 0, end=" ")
            print()
        print()

        X = lupSolve(L, U, P, b)
        print("Solution Vector X:")
        for i in range(n):
            print(f"x{i + 1} = {X[i]:.3f}")
        print()

        A_inv = inverse(L, U, P)
        printMatrix(A_inv, "Inverse Matrix")