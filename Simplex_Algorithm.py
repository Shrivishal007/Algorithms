"""
Problem: Solve a Linear Programming maximization problem.
Approach: Simplex Algorithm (Tableau Method).
Assumptions: Standard maximum form LP (Maximization objective, all constraints are <=, RHS bounds >= 0).
Input: Objective coefficients 'c', constraint matrix 'A', constraint bounds 'b'.
Output: Optimal solution vector and optimal objective value.
Time Complexity: Exponential worst-case O(2^n), but typically polynomial O(m^3) in practice.
Space Complexity: O(m * (n + m)) to store the Simplex tableau.
Key Idea: 

"""

def simplex(c, A, b, max_iter=10):
    # m = number of constraints, n = number of decision variables
    m, n = len(A), len(A[0])
    
    # Tableau has m+1 rows (constraints + Z row) and n+m+1 columns (vars + slacks + RHS)
    tableau = [[0] * (n + m + 1) for _ in range(m + 1)]

    # 1. Initialize constraints and slack variables
    for i in range(m):
        for j in range(n):
            tableau[i][j] = A[i][j]
        tableau[i][n + i] = 1  # Identity matrix for slack variables
        tableau[i][n + m] = b[i] # RHS values

    # 2. Initialize Z row (objective function) with -c
    for j in range(n):
        tableau[m][j] = -c[j]

    iteration = 1 

    # 3. Main Simplex loop
    while iteration <= max_iter:
        found = False
        # Check for optimality: if all Z-row coefficients are >= 0, we are done
        for j in range(n + m):
            if tableau[m][j] < 0:
                found = True
                break

        if not found:
            break

        print(f"\nIteration {iteration}")
        printTableau(tableau, n, m)

        # Entering variable: column with the most negative value in Z row
        pivot_col = 0
        for j in range(1, n + m):
            if tableau[m][j] < tableau[m][pivot_col]:
                pivot_col = j

        bounded = False
        for i in range(m):
            if tableau[i][pivot_col] > 0:
                bounded = True
                break

        if not bounded:
            raise ValueError('Unbounded solution')

        # Leaving variable: row with the minimum positive ratio of RHS / pivot_column_value
        pivot_row = -1
        min_ratio = float('inf')
        for i in range(m):
            if tableau[i][pivot_col] > 0:
                ratio = tableau[i][n + m] / tableau[i][pivot_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i

        if pivot_row == -1:
            raise ValueError('Unbounded solution')

        # 4. Perform Pivot Operations (Gaussian Elimination)
        pivot = tableau[pivot_row][pivot_col]
        
        # Normalize the pivot row
        for j in range(n + m + 1):
            tableau[pivot_row][j] /= pivot

        # Eliminate pivot column entries in all other rows
        for i in range(m + 1):
            if i != pivot_row:
                factor = tableau[i][pivot_col]
                for j in range(n + m + 1):
                    tableau[i][j] -= factor * tableau[pivot_row][j]

        print(f"\nPivot Row = {pivot_row + 1}, Pivot Column = {pivot_col + 1}")
        printTableau(tableau, n, m)

        iteration += 1

    if iteration > max_iter:
        print("\nMaximum iterations reached.")

    # 5. Extract optimal solution
    solution = [0] * n
    for j in range(n):
        ones = [i for i in range(m) if tableau[i][j] == 1]
        zeros = [i for i in range(m) if tableau[i][j] == 0]
        
        # If the column represents a basic variable (one 1, the rest 0s)
        if len(ones) == 1 and len(zeros) == m - 1:
            solution[j] = tableau[ones[0]][n + m]

    optimum_value = tableau[m][n + m]

    return solution, optimum_value

def printTableau(tableau, n, m):
    for j in range(n):
        print(f"{f'x_{j + 1}':>6}", end=" ")
    for j in range(m):
        print(f"{f's_{j + 1}':>6}", end=" ")
    print(f"|{'RHS':>6}")

    print("-" * ((n + m + 1) * 7))

    for i in range(m + 1):
        if i == m:
            print("-" * ((n + m + 1) * 7))

        for j in range(n + m + 1):
            if n + m == j:
                print("|", end="")
            print(f"{tableau[i][j]:6.2f}", end=" ")

        if i == m:
            print(f"\t(Z row)")
        else:
            print()

if __name__ == "__main__":
    c = list(map(int, input("Enter c values: ").split()))
    b = list(map(int, input("Enter b values: ").split()))
    m = len(b)
    n = len(c)

    A = []
    print("Enter A matrix: ")
    for i in range(m):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        A.append(row)

    print("\nMaximize Z: ", end="")
    for j in range(n):
        sign = " + " if j > 0 and c[j] >= 0 else " "
        print(f"{sign}{c[j]} x_{j+1}", end="")
    print()

    print("Subject to:")
    for i in range(m):
        for j in range(n):
            sign = " + " if j > 0 and A[i][j] >= 0 else " "
            print(f"{sign}{A[i][j]} x_{j+1}", end="")
        print(f" ≤ {b[i]}")
    print(", ".join([f"x{i+1}" for i in range(n)]) + " ≥ 0")

    try:
        solution, value = simplex(c, A, b)
    except ValueError as e:
        print("Simplex failed:", e)
    else:
        print(f"\nOptimal solution : {solution}")
        print(f"Optimal value = {value}")