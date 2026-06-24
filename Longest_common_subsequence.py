"""
Problem: Find the Longest Common Subsequence (LCS) between two strings.
Approach: Bottom-up Dynamic Programming.
Assumptions: The inputs are iterables containing comparable elements. 
Input: Two strings 'X' and 'Y'.
Output: A 2D DP table representing LCS lengths at each prefix, and the reconstructed LCS string printed to console.
Time Complexity: O(m * n), where m and n are the lengths of strings X and Y.
Space Complexity: O(m * n) to store the DP table.
Key Idea: 
If X[i-1] == Y[j-1]:
    dp[i][j] = 1 + dp[i-1][j-1]
Else:
    dp[i][j] = max(
        dp[i-1][j],             // skip from X
        dp[i][j-1]              // skip from Y
    )
Base cases:
dp[0][j] = 0 for all j
dp[i][0] = 0 for all i
"""

def LCSLength(X, Y):
    m, n = len(X), len(Y)

    # Initialize DP table with zeros
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        print(f"\ni = {i}")

        for j in range(1, n + 1):
            print(f"j = {j}, ", end="")

            # Characters match: sequence length increases by 1 relative to the prefix without either character
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1

                print(f"{X[i - 1]} == {Y[j - 1]} ==> c[{i}][{j}] = {c[i - 1][j - 1]} + 1 = {c[i - 1][j - 1] + 1}")

            # Characters differ: inherit the maximum sequence length found so far
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

                print(f"{X[i - 1]} != {Y[j - 1]} ==> c[{i}][{j}] = max{c[i - 1][j], c[i][j - 1]} = {max(c[i - 1][j], c[i][j - 1])}")

    print()

    return c

def printLCS(c, X, Y, i, j):
    # Base case: reached the beginning of either string
    if i == 0 or j == 0:
        return

    # If characters matched, they are part of the LCS. Recurse diagonally and print.
    if X[i - 1] == Y[j - 1]:
        printLCS(c, X, Y, i - 1, j - 1)
        print(f"{X[i - 1]:2}", end="")

    # If they didn't match, trace back to the cell that gave the maximum value.
    # Prioritize moving Up (ignoring character in X) on a tie.
    elif c[i - 1][j] >= c[i][j - 1]:
        printLCS(c, X, Y, i - 1, j)

    # Otherwise, move Left (ignoring character in Y)
    else:
        printLCS(c, X, Y, i, j - 1)

if __name__ == "__main__":
    X = input("Enter String1: ").upper()
    Y = input("Enter String2: ").upper()
    m = len(X)
    n = len(Y)

    c = LCSLength(X, Y)

    # Print DP Table with values
    for j in range(-2, n):
        if j < 0:
            print(" " * 2, end="")
        else:
            print(f"{Y[j]:2}", end="")
    print()
    for i in range(m + 1):
        if i == 0:
            print(" ", end="")
        else:
            print(X[i - 1], end="")

        for j in range(n + 1):
            print(f"{c[i][j]:2}", end="")
        print()
    print()

    # Print DP Table with directional arrows
    for j in range(-2, n):
        if j < 0:
            print(" " * 2, end="")
        else:
            print(f"{Y[j]:2}", end="")
    print()
    for i in range(m + 1):
        if i == 0:
            print(" ", end="")
        else:
            print(X[i - 1], end="")

        for j in range(n + 1):
            if i == 0:
                print(f"{j:2}", end="")
            elif j == 0:
                print(f"{i:2}", end="")
            else:
                # Reconstruct path logic perfectly matches printLCS conditions
                if X[i - 1] == Y[j - 1]:
                    char = "↖"
                elif c[i - 1][j] >= c[i][j - 1]:
                    char = "↑"
                else:
                    char = "←"
                
                print(f"{char:>2}", end="")
        print()
    print()

    print(f"Length: {c[m][n]}")
    print("Common String:", end=" ")
    printLCS(c, X, Y, m, n)