"""
Problem: Compute the Edit Distance (Levenshtein Distance) between two strings.
Approach: Bottom-up Dynamic Programming.
Assumptions: Insert, Delete, and Replace operations all have a uniform cost of 1.
Input: Two strings 'X' (Source) and 'Y' (Target).
Output: A 2D DP table representing the distances, and a sequence of operations printed to the console.
Time Complexity: O(m * n), where m and n are the lengths of strings X and Y.
Space Complexity: O(m * n) to store the DP table.
Key Idea: 
If X[i-1] == Y[j-1]:
    dp[i][j] = dp[i-1][j-1]
Else:
    dp[i][j] = 1 + min(
        dp[i-1][j],    // delete
        dp[i][j-1],    // insert
        dp[i-1][j-1]   // replace
    )
Base cases:
dp[0][j] = j for all j
dp[i][0] = i for all i
"""

def editDistance(X, Y):
    m, n = len(X), len(Y)

    # Initialize DP table with zeros
    D = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: transforming a string to an empty string requires deleting all characters
    for i in range(m + 1):
        D[i][0] = i
    # Base cases: transforming an empty string to a string requires inserting all characters
    for j in range(n + 1):
        D[0][j] = j

    for i in range(1, m + 1):
        print(f"\ni = {i}")

        for j in range(1, n + 1):
            print(f"\tj = {j}, ", end="")

            # Characters match: cost is 0, inherit distance from the diagonal (i-1, j-1)
            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1]

                print(f"{X[i - 1]} == {Y[j - 1]} ==> D[{i}][{j}] = D[{i - 1}][{j - 1}] = {D[i][j]}")

            # Characters differ: calculate cost of 3 possible operations and take the minimum
            else:
                insert_cost = D[i][j - 1]
                delete_cost = D[i - 1][j]
                replace_cost = D[i - 1][j - 1]
                D[i][j] = 1 + min(insert_cost, delete_cost, replace_cost)

                print(f"{X[i - 1]} != {Y[j - 1]} ==> D[{i}][{j}] = min{insert_cost, delete_cost, replace_cost} + 1 = {D[i][j]}")

    print()

    return D

def printOperations(D, X, Y, i, j):
    # Base case: reached the beginning of both strings
    if i == 0 and j == 0:
        return

    # If X is exhausted, we can only insert remaining Y characters
    if i == 0:
        printOperations(D, X, Y, i, j - 1)
        print(f"Insert {Y[j - 1]}")
    # If Y is exhausted, we can only delete remaining X characters
    elif j == 0:
        printOperations(D, X, Y, i - 1, j)
        print(f"Delete {X[i - 1]}")
    # Check which operation led to the current minimum distance
    elif D[i][j] == D[i][j - 1] + 1:
        printOperations(D, X, Y, i, j - 1)
        print(f"Insert {Y[j - 1]}")
    elif D[i][j] == D[i - 1][j] + 1:
        printOperations(D, X, Y, i - 1, j)
        print(f"Delete {X[i - 1]}")
    else:
        printOperations(D, X, Y, i - 1, j - 1)
        if X[i - 1] != Y[j - 1]:
            print(f"Replace {X[i - 1]} with {Y[j - 1]}")

if __name__ == "__main__":
    X = input("Enter Source string: ").upper()
    Y = input("Enter Target string: ").upper()
    m = len(X)
    n = len(Y)

    D = editDistance(X, Y)

    # Print DP Table with numerical costs
    for j in range(-2, n):
        if j < 0:
            print(" " * 3, end="")
        else:
            print(f"{Y[j]:3}", end="")
    print()
    for i in range(m + 1):
        if i == 0:
            print(" ", end="")
        else:
            print(X[i - 1], end="")

        for j in range(n + 1):
            print(f"{D[i][j]:3}", end="")
        print()
    print()

    # Print DP Table with directional arrows
    for j in range(-2, n):
        if j < 0:
            print(" " * 3, end="")
        else:
            print(f"{Y[j]:3}", end="")
    print()
    for i in range(m + 1):
        if i == 0:
            print(" ", end="")
        else:
            print(X[i - 1], end="")

        for j in range(n + 1):
            if i == 0:
                print(f"{j:3}", end="")
            elif j == 0:
                print(f"{i:3}", end="")
            else:
                if D[i][j] == D[i][j - 1] + 1:
                    char = "←"
                elif D[i][j] == D[i - 1][j] + 1:
                    char = "↑"
                else:
                    char = "↖"

                print(f"{char:>3}", end="")
        print()
    print()

    print(f"Length: {D[m][n]}")
    print("Operations:")
    printOperations(D, X, Y, m, n)