def lup_decomposition(A):
    n = len(A)
    a = [row[:] for row in A]
    P = list(range(n))

    for k in range(n - 1):
        pivot = abs(a[k][k])
        k_i = k

        for i in range(k, n):
            if abs(a[i][k]) > pivot:
                pivot = abs(a[i][k])
                k_i = i

        if pivot == 0:
            raise ValueError('Singular matrix')

        a[k], a[k_i] = a[k_i], a[k]
        P[k], P[k_i] = P[k_i], P[k]

        for i in range(k + 1, n):
            a[i][k] /= a[k][k]
            for j in range(k + 1, n):
                a[i][j] -= a[i][k] * a[k][j]

    if a[n - 1][n - 1] == 0:
        raise ValueError('Singular matrix')

    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
        for j in range(i):
            L[i][j] = a[i][j]

        for j in range(i, n):
            U[i][j] = a[i][j]

    return L, U, P

def lup_solve(L, U, P, B):
    n = len(L)
    
    PB = [0] * n
    for i in range(n):
        PB[i] = B[P[i]]

    Y = [0] * n
    for i in range(n):
        summation = 0
        for j in range(i):
            summation += L[i][j] * Y[j]
        Y[i] = PB[i] - summation

    X = [0] * n
    for i in range(n - 1, -1, -1):
        summation = 0
        for j in range(i + 1, n):
            summation += U[i][j] * X[j]
        X[i] = (Y[i] - summation) / U[i][i]

    return X

def inverse(A):
    n = len(A)
    L, U, P = lup_decomposition(A)
    A_inv = [[0] * n for _ in range(n)]

    for j in range(n):
        B_j = [0] * n
        B_j[j] = 1
        X_j = lup_solve(L, U, P, B_j)

        for i in range(n):
            A_inv[i][j] = X_j[i]

    return A_inv

def print_matrix(m, name):
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
        L, U, P = lup_decomposition(A)

    except ValueError as e:
        print("LUP decomposition failed:", e)

    else:
        print_matrix(L, "L Matrix")
        print()
        print_matrix(U, "U Matrix")
        print()
        print("P Matrix:")
        for i in range(n):
            for j in range(n):
                print(1 if P[i] == j else 0, end=" ")
            print()
        print()

        X = lup_solve(L, U, P, b)
        print("Solution Vector X:")
        for i in range(n):
            print(f"x{i + 1} = {X[i]:.3f}")
        print()

        A_inv = inverse(A)
        print_matrix(A_inv, "Inverse Matrix")