"""
Problem: 0/1 Knapsack Problem.
Approach: Bottom-up Dynamic Programming.
Assumptions: Weights and values are non-negative integers. Each item can be picked at most once.
Input: Total capacity 'W', list of weights 'w', list of profits 'v'.
Output: A 2D DP table representing maximum profit, and the selected items printed to the console.
Time Complexity: O(N * W), where N is the number of items and W is the capacity.
Space Complexity: O(N * W) to store the DP table (necessary for backtracing selected items).
Key Idea: 
If w[i-1] <= j:
    dp[i][j] = max(
        dp[i-1][j],                         // exclude item i
        v[i-1] + dp[i-1][j - w[i-1]]        // include item i
    )
Else:
    dp[i][j] = dp[i-1][j]                   // item i cannot be included
Base cases:
dp[0][j] = 0 for all j
dp[i][0] = 0 for all i
"""

def knapsack(W, w, v):
    N = len(v)

    # Initialize DP table with zeros. DP[i][j] represents max profit for first 'i' items with capacity 'j'
    DP = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        print(f"\ni = {i}, w[{i - 1}] = {w[i - 1]}, v[{i - 1}] = {v[i - 1]}")

        for j in range(1, W + 1):
            print(f"\tj = {j}, ", end="")

            # If the current item's weight is less than or equal to current capacity, we have a choice
            if w[i - 1] <= j:
                # Max of excluding the item vs. including the item
                DP[i][j] = max(DP[i - 1][j], v[i - 1] + DP[i - 1][j - w[i - 1]])

                print(f"{w[i - 1]} ≤ {j} ==> DP[{i}][{j}] = max{DP[i - 1][j], v[i - 1] + DP[i - 1][j - w[i - 1]]} = {DP[i][j]}")

            # Item is too heavy to include, inherit max profit from the previous item at this capacity
            else:
                DP[i][j] = DP[i - 1][j]

                print(f"{w[i - 1]} > {j} ==> DP[{i}][{j}] = DP[{i - 1}][{j}] = {DP[i][j]}")
    print()

    return DP

def printItems(DP, w, S, i, j):
    # Base case: reached the top of the table or capacity is exactly 0
    if i == 0 or j == 0:
        return

    # If the profit came from the row above, the current item was NOT included
    if DP[i][j] != DP[i - 1][j]:
        S[i - 1] = 1 # Mark item as selected
        # Move up one row, and subtract the item's weight from capacity
        printItems(DP, w, S, i - 1, j - w[i - 1])

    else:
        # Move up one row, capacity remains the same
        printItems(DP, w, S, i - 1, j)

if __name__ == "__main__":
    w = list(map(int, input("Enter the weight values: ").split()))
    v = list(map(int, input("Enter the profit values: ").split()))

    if len(w) != len(v):
        raise ValueError('Number of weights and profits must be equal')

    W = int(input("Enter total capacity: "))
    N = len(w)

    # State array to keep track of selected items
    S = [0] * N

    DP = knapsack(W, w, v)

    # Print DP Table
    for j in range(-1, W + 1):
        if j < 0:
            print(" ", end="")
        else:
            print(f"{j:4}", end="")
    print()
    
    for i in range(N + 1):
        print(i, end="")
        for j in range(W + 1):
            print(f"{DP[i][j]:4}", end="")
        print()
    print()

    print(f"Total Profit: {DP[N][W]}")

    # Traceback to find and print selected items
    printItems(DP, w, S, N, W)
    for i in range(N):
        if S[i] == 1:
            print(f"Item {i + 1} is selected")